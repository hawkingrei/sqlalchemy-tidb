import pytest
from sqlalchemy.dialects import registry

registry.register(
    "tidb",
    "sqlalchemy_tidb.mysqlconnector",
    "TiDBDialect_mysqlconnector"
)

# sqlalchemy's dialect-testing machinery wants an entry like this.
# It is wack. :(
registry.register(
    "tidb.mysqlconnector",
    "sqlalchemy_tidb.mysqlconnector",
    "TiDBDialect_mysqlconnector",
)

pytest.register_assert_rewrite("sqlalchemy.testing.assertions")

from sqlalchemy.testing.plugin.pytestplugin import *  # noqa
