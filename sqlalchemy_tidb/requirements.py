from sqlalchemy.testing.requirements \
    import SuiteRequirements as SuiteRequirementsSQLA
from alembic.testing.requirements \
    import SuiteRequirements as SuiteRequirementsAlembic

from sqlalchemy.testing import exclusions


class Requirements(SuiteRequirementsSQLA, SuiteRequirementsAlembic):
    temporary_tables = exclusions.closed()
    temp_table_reflection = exclusions.closed()
