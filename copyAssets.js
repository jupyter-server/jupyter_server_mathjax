const fse = require("fs-extra");
const path = require("path");

const srcDir = path.join(__dirname, "node_modules", "mathjax");
const dstDir = path.join(__dirname, "jupyter_server_mathjax", "static");

/*
 * Copy MathJax static assets, but trim which assets in a similar way to what
 * notebook does on dist (in setupbase).
 */

const rps = path.sep.replace("\\", "\\\\");

function re_join(parts) {
  return parts.join(rps);
}

const include = [
  ["MathJax.js"],
  ["LICENSE"],
  ["config", "TeX-AMS-MML_HTMLorMML-full.js"],
  ["config", "Safe.js"],
];

const re_include = [
  ["jax", "output", `[^${rps}]+.js$`],
  ["jax", "output", "autoload", ".*"],
  ["localization", ".*"],
  ["fonts", "HTML-CSS", "STIX-Web", "woff", ".*"],
  ["extensions", ".*"],
  ["jax", "input", "TeX", ".*"],
  ["jax", "output", "HTML-CSS", "fonts", "STIX-Web", ".*"],
  ["jax", "output", "SVG", "fonts", "STIX-Web", ".*"],
  ["jax", "element", "mml", ".*"],
];

function isPartial(parts, candidate) {
  return parts.length <= candidate.length;
}

function partialPathMatch(parts, candidate) {
  const np = Math.min(candidate.length, parts.length);
  for (let i = 0; i < np; ++i) {
    if (candidate[i] !== parts[i]) {
      return false;
    }
  }
  return true;
}

function pathOk(p) {
  if (!p) {
    return true;
  }
  const parts = p.split(path.sep);
  for (let c of include) {
    if (isPartial(parts, c)) {
      // Check for partial matches (to ensure dirs get included)
      if (partialPathMatch(parts, c)) {
        return true;
      }
    } else {
      if (c.join(path.sep) == p) {
        return true;
      }
    }
  }
  for (let c of re_include) {
    const lead = c.slice(0, c.length - 1);
    if (isPartial(parts, lead)) {
      // Check for partial matches (to ensure dirs get included)
      if (partialPathMatch(parts, lead)) {
        return true;
      }
    } else {
      const re = new RegExp(re_join(c));
      if (re.test(p)) {
        return true;
      }
    }
  }
  return false;
}

function filterFunc(src, dest) {
  const relative = path.relative(srcDir, src);
  return pathOk(relative);
}

fse.copy(srcDir, dstDir, { filter: filterFunc });
