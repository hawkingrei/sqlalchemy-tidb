from sqlalchemy import util
from sqlalchemy.dialects.mysql.base import BIT
from sqlalchemy.dialects.mysql.cymysql \
    import MySQLDialect_cymysql, _cymysqlBIT

from .base import TiDBDialect


class TiDBDialect_cymysql(MySQLDialect_cymysql):
    driver = "cymysql"

    colspecs = util.update_copy(TiDBDialect.colspecs, {BIT: _cymysqlBIT})


dialect = TiDBDialect_cymysql
