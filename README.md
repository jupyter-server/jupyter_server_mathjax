# MathJax resources endpoints for Jupyter Server

![Testing](https://github.com/jupyter-server/jupyter_server_mathjax/workflows/Testing/badge.svg)



## Basic Usage

Install from PyPI:

```sh
> pip install jupyter_server_mathjax
```

This will automatically enable the extension in Jupyter Server.

To test the installation, you can run Jupyter Server and visit the `/static/jupyter_server_mathjax/MathJax.js` endpoint:

```sh
> jupyter server
```

## Maintenance Notes

To install an editable install locally for development, first clone the repository locally,
then run:

```sh
`pip install -e .[test]`
```

Note that the editable install will not install the data file that
automatically configures the extension for use. To manually enable it, run:

```sh
jupyter server extension enable --py jupyter_server_mathjax
```

To build for distribution, use the `build` package:

```sh
pip install build
python -m build
```

Then release using twine:

```sh
twine check dist/*
twine check dist/*
```
