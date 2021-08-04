import pytest
from sqlalchemy.dialects import registry

registry.register(
    "tidb",
    "sqlalchemy_tidb.mysqldb",
    "TiDBDialect_mysqldb"
)

# sqlalchemy's dialect-testing machinery wants an entry like this.
# It is wack. :(
registry.register(
    "tidb.mysqldb",
    "sqlalchemy_tidb.mysqldb",
    "TiDBDialect_mysqldb",
)

pytest.register_assert_rewrite("sqlalchemy.testing.assertions")

from sqlalchemy.testing.plugin.pytestplugin import *  # noqa
