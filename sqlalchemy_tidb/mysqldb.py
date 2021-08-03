from sqlalchemy.dialects.mysql.mysqldb \
    import MySQLDialect_mysqldb

from .base import TiDBCompiler
from .base import TiDBDDLCompiler
from .base import TiDBDialect
from .base import TiDBIdentifierPreparer


class TiDBDialect_mysqldb(MySQLDialect_mysqldb, TiDBDialect):
    name = "tidb"
    driver = "mysqldb"
    supports_statement_cache = True

    supports_unicode_binds = True

    supports_sane_rowcount = True
    supports_sane_multi_rowcount = True

    supports_native_decimal = True

    default_paramstyle = "format"
    ddl_compiler = TiDBDDLCompiler
    statement_compiler = TiDBCompiler

    preparer = TiDBIdentifierPreparer


dialect = TiDBDialect_mysqldb
