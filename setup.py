from os.path import realpath, dirname, join as path_join
from setuptools import setup, find_packages

NAME = "sse"
DESCRIPTION = "Semantic Search Engine for PubMed"
LONG_DESCRIPTION = ""
URL = "https://github.com/escodebar/sse"
license = "GPL"
VERSION = "1.0"

PROJECT_ROOT = dirname(realpath(__file__))
REQUIREMENTS_FILE = path_join(PROJECT_ROOT, "requirements.txt")

with open(REQUIREMENTS_FILE, "r") as f:
    INSTALL_REQUIREMENTS = [
        requirement for requirement in f.read().splitlines()
    ]

SETUP_REQUIREMENTS = ["pytest-runner"]
TEST_REQUIREMENTS = ["pytest", "pytest-cov", "hypothesis"]

if __name__ == "__main__":
    setup(
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        url=URL,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        package_data={"docs": ["*"]},
        include_package_data=True,
        install_requires=INSTALL_REQUIREMENTS,
        setup_requires=SETUP_REQUIREMENTS,
        tests_require=TEST_REQUIREMENTS,
    )

