from setuptools import setup
import _version
    
def readme():
    with open("docs/index.md") as f:
        return f.read()

setup(
    name="ModelRollout",
    version=_version.__version__,
    description="Realstats model version control",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/bharkema/RealstatsModelRollout",
    download_url = 'https://github.com/bharkema/RealstatsModelRollout/archive/' + _version.__version__ + '.tar.gz',
    author="Bowen",
    author_email="b.harkema@clappform.com",
    keywords="model validation",
    license="MIT",
    packages = ['ModelRollout'],
    install_requires=[
        "pandas",
        "pyarrow",
        "pygithub"
    ],
    include_package_data=True,
)