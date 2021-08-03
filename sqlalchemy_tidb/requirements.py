from sqlalchemy.testing.requirements \
    import SuiteRequirements as SuiteRequirementsSQLA
from alembic.testing.requirements \
    import SuiteRequirements as SuiteRequirementsAlembic


class Requirements(SuiteRequirementsSQLA, SuiteRequirementsAlembic):
    pass
