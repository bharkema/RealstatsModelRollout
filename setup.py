from setuptools import setup
import _version_

def readme():
    with open("Documentation/main.md") as f:
        return f.read()

setup(
    name="Clappform",
    version=_version_.__version__,
    description="Realstats Model Rollout",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Unstable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    url="",
    download_url = '' + _version_.__version__ + '.tar.gz',
    author="Realstats",
    author_email="",
    keywords="model validation",
    license="MIT",
    packages = ['RealstatsModelRollout'],
    install_requires=[
        "pandas"
    ],
    include_package_data=True,
)