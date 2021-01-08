To create a release, update the version number in `jupyter_server_mathjax/__version__.py`, then run the following:

```
git clean -dffx
python setup.py sdist bdist_wheel
export script_version=`python setup.py --version 2>/dev/null`
git commit -a -m "Release $script_version"
git tag $script_version
pip install twine
twine check dist/*
twine upload dist/*
git push --all
git push --tags
```
