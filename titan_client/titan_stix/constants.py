import re

from stix2 import TLP_AMBER

REMOVE_HTML_REGEX = re.compile(r"<.*?>")
X_OPENCT_CREATED_BY = "x_opencti_created_by_ref"
MARKING = TLP_AMBER
INTEL_471 = "Intel 471"