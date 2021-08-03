from sqlalchemy.dialects import registry as _registry

__version__ = "1.0.0"

_registry.register(
    "tidb.mysqlconnector",
    "sqlalchemy_tidb.mysqlconnector",
    "TiDBDialect_mysqlconnector",
)
