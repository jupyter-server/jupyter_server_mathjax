from pathlib import Path
from setuptools import find_packages, setup
from jupyter_packaging import (
    combine_commands,
    create_cmdclass,
    ensure_targets,
    get_version,
    install_npm,
)


NAME = "jupyter_server_mathjax"

here = Path(__file__).absolute().parent
project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
version = get_version(here / NAME / "__version__.py")


with open("README.md", "r") as fh:
    long_description = fh.read()

jstargets = [
    here.joinpath(NAME, 'static', 'MathJax.js'),
    here.joinpath(NAME, 'static', 'LICENSE'),  # We need to include the license if we are distributing MathJax
]

# Handle datafiles
cmdclass = create_cmdclass(
    "js",
    data_files_spec=[
        ("etc/jupyter/jupyter_server_config.d", "jupyter_server_config.d", "*.json")
    ],
)

cmdclass["js"] = combine_commands(
    install_npm(here),
    ensure_targets(jstargets),
)

setup_args = dict(
    name=NAME,
    description="MathJax resources as a Jupyter Server Extension.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=version,
    packages=find_packages(exclude=["tests*"]),
    author="Jupyter Development Team",
    author_email="jupyter@googlegroups.com",
    url="http://jupyter.org",
    license="BSD",
    platforms="Linux, Mac OS X, Windows",
    keywords=["ipython", "jupyter", "jupyter-server"],
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    cmdclass=cmdclass,
    zip_safe=False,
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=[
        "jupyter_server~=1.1",
    ],
    extras_require={
        "test": [
            "jupyter_server[test]",
            "pytest",
        ],
    },
)

if __name__ == "__main__":
    setup(**setup_args)
