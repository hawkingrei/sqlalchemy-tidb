from sqlalchemy import util
from sqlalchemy.dialects.mysql.base import BIT
from sqlalchemy.dialects.mysql.oursql \
    import MySQLDialect_oursql, _oursqlBIT
from sqlalchemy.sql import sqltypes

from .base import TiDBDialect


class TiDBDialect_oursql(MySQLDialect_oursql, TiDBDialect):
    colspecs = util.update_copy(
        TiDBDialect.colspecs, {sqltypes.Time: sqltypes.Time, BIT: _oursqlBIT}
    )


dialect = TiDBDialect_oursql
