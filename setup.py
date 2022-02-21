# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from pathlib import Path
from setuptools import setup
from jupyter_packaging import (
    wrap_installers,
    npm_builder,
    get_version,
)


NAME = "jupyter_server_mathjax"
here = Path(__file__).absolute().parent
version = get_version(here / NAME / "__version__.py")

jstargets = [
    here.joinpath(NAME, "static", "MathJax.js"),
    # if we are distributing MathJax, we need to include its license:
    here.joinpath(NAME, "static", "LICENSE"),
]

# Handle datafiles
builder = npm_builder(here)
cmdclass = wrap_installers(
    pre_develop=builder,
    pre_dist=builder,
    ensured_targets=jstargets
)

setup_args = dict(
    version=version,
    cmdclass=cmdclass,
)

if __name__ == "__main__":
    setup(**setup_args)
