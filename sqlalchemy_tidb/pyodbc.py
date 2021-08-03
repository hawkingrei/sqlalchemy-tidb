from sqlalchemy import util
from sqlalchemy.dialects.mysql.pyodbc \
    import MySQLDialect_pyodbc, _pyodbcTIME
from sqlalchemy.sql.sqltypes import Time

from .base import TiDBDialect


class TiDBDialect_pyodbc(MySQLDialect_pyodbc, TiDBDialect):
    colspecs = util.update_copy(TiDBDialect.colspecs, {Time: _pyodbcTIME})


dialect = TiDBDialect_pyodbc
