import os
from linkedin import Linkedin

EMAIL = os.environ['LINKEDIN_EMAIL']
PASSWORD = os.environ['LINKEDIN_PASSWORD']
JOB_DESCRIPTION = "Software Developer"
LOCATION_COUNTRY = "Türkiye"

linkedin = Linkedin()
linkedin.login(EMAIL,PASSWORD)
linkedin.search_for_jobs(JOB_DESCRIPTION,
                         LOCATION_COUNTRY)
linkedin.job_applier()


