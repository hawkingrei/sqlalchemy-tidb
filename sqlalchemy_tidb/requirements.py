from sqlalchemy.testing.requirements \
    import SuiteRequirements as SuiteRequirementsSQLA
from alembic.testing.requirements \
    import SuiteRequirements as SuiteRequirementsAlembic

from sqlalchemy.testing import exclusions, skip_if, fails_if, only_on


class Requirements(SuiteRequirementsSQLA, SuiteRequirementsAlembic):
    temporary_tables = exclusions.closed()
    temp_table_reflection = exclusions.closed()
    order_by_label_with_expression = exclusions.closed()
    order_by_col_from_union = exclusions.closed()
    time_microseconds = exclusions.closed()
    foreign_keys = exclusions.closed()

    @property
    def datetime_microseconds(self):
        """target dialect supports representation of Python
        datetime.datetime() with microsecond objects."""

        return skip_if(
            ["tidb"]
        )

    @property
    def unbounded_varchar(self):
        """Target database must support VARCHAR with no length"""

        return skip_if(
            ["firebird", "oracle", "mysql", "mariadb", "tidb"],
            "not supported by database",
        )

    @property
    def independent_cursors(self):
        """Target must support simultaneous, independent database cursors
        on a single connection."""

        return skip_if(["tidb"], "no driver support")

    @property
    def self_referential_foreign_keys(self):
        """Target database must support self-referential foreign keys."""

        return exclusions.closed()

    @property
    def foreign_key_constraint_reflection(self):
        return exclusions.closed()

    @property
    def implicitly_named_constraints(self):
        return exclusions.open()

    @property
    def precision_generic_float_type(self):
        """target backend will return native floating point numbers with at
        least seven decimal places when using the generic Float type."""

        return fails_if(
            [
                (
                    "tidb",
                    None,
                    None,
                    "tidb FLOAT type only returns 4 decimals",
                ),
            ]
        )

    @property
    def sql_expression_limit_offset(self):
        return (
            fails_if(
                ["tidb"],
                "Target backend can't accommodate full expressions in "
                "OFFSET or LIMIT",
            )
            + self.offset
        )

