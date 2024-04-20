import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME="Text-Summarization"
AUTHON_USER_NAME = "prithviraj-kt"
SRC_REPO = "textSummarizer"
AUTHON_EMAIL="prithvirajktagadinamani@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    authon=AUTHON_USER_NAME,
    author_email=AUTHON_EMAIL,
    description=" A small package for text summarization, basically tradition CNN",
    ong_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHON_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHON_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)