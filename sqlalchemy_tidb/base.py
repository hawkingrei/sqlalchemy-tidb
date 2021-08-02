from sqlalchemy import util
from sqlalchemy.dialects.mysql.base import MySQLDialect, MySQLCompiler, MySQLDDLCompiler, MySQLTypeCompiler, \
    MySQLIdentifierPreparer
from sqlalchemy.engine import default


class TiDBCompiler(MySQLCompiler):
    pass


class TiDBDDLCompiler(MySQLDDLCompiler):
    pass


class TiDBTypeCompiler(MySQLTypeCompiler):
    pass


class TiDBIdentifierPreparer(MySQLIdentifierPreparer):
    pass


class TiDBDialect(MySQLDialect):
    name = "tidb"
    supports_sequences = True
    supports_for_update_of = True

    statement_compiler = TiDBCompiler
    ddl_compiler = TiDBDDLCompiler
    type_compiler = TiDBTypeCompiler
    preparer = TiDBIdentifierPreparer

    def initialize(self, connection):
        self._connection_charset = self._detect_charset(connection)
        self._detect_sql_mode(connection)
        self._detect_ansiquotes(connection)
        self._detect_casing(connection)
        if self._server_ansiquotes:
            # if ansiquotes == True, build a new IdentifierPreparer
            # with the new setting
            self.identifier_preparer = self.preparer(
                self, server_ansiquotes=self._server_ansiquotes
            )

        default.DefaultDialect.initialize(self, connection)

    def _get_server_version_info(self, connection):
        # get database server version info explicitly over the wire
        # to avoid proxy servers like MaxScale getting in the
        # way with their own values, see #4205
        dbapi_con = connection.connection
        cursor = dbapi_con.cursor()
        cursor.execute("SELECT VERSION()")
        val = cursor.fetchone()[0]
        cursor.close()
        if util.py3k and isinstance(val, bytes):
            val = val.decode()

        return self._parse_server_version(val)

    def _parse_server_version(self, val):
        version_list = val.split('-')
        tidb_version_list = version_list[2].lstrip('v').split('.')
        server_version_info = tuple(int(x) for x in tidb_version_list)
        self.server_version_info = server_version_info
        return server_version_info
