const fse = require('fs-extra')
const path = require('path');

const srcDir = path.join(__dirname, 'node_modules', 'mathjax');
const dstDir = path.join(__dirname, 'jupyter_server_mathjax', 'static');
// Exclude unneeded files:
const exclude = ['unpacked', 'test', 'package.json', 'README.md', 'CONTRIBUTING.md', 'latest.js'];

function inSubDir(candidate, root) {
  const relative = path.relative(root, path.dirname(candidate));
  return relative && !relative.startsWith('..') && !path.isAbsolute(relative);
}

function filterFunc(src, dest) {
  const relative = path.relative(srcDir, src);
  const sub = inSubDir(src, srcDir);
  return sub || exclude.indexOf(relative) === -1;
}

fse.copy(srcDir, dstDir, {filter: filterFunc});


// TODO: Trim to same resources as notebook?
/*
# Trim mathjax
mj = lambda *path: pjoin(components, 'MathJax', *path)
static_data.extend([
    mj('MathJax.js'),
    mj('config', 'TeX-AMS-MML_HTMLorMML-full.js'),
    mj('config', 'Safe.js'),
])

trees = []
mj_out = mj('jax', 'output')

if os.path.exists(mj_out):
    for output in os.listdir(mj_out):
        path = pjoin(mj_out, output)
        static_data.append(pjoin(path, '*.js'))
        autoload = pjoin(path, 'autoload')
        if os.path.isdir(autoload):
            trees.append(autoload)

for tree in trees + [
    mj('localization'), # limit to en?
    mj('fonts', 'HTML-CSS', 'STIX-Web', 'woff'),
    mj('extensions'),
    mj('jax', 'input', 'TeX'),
    mj('jax', 'output', 'HTML-CSS', 'fonts', 'STIX-Web'),
    mj('jax', 'output', 'SVG', 'fonts', 'STIX-Web'),
    mj('jax', 'element', 'mml'),
]:
    for parent, dirs, files in os.walk(tree):
        for f in files:
            static_data.append(pjoin(parent, f))
*/
