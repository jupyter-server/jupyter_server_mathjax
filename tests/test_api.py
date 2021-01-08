"""Basic tests for the notebook handlers.
"""


async def test_mathjax_mainjs_handler(jp_fetch):
    r = await jp_fetch('static', 'components', 'MathJax', 'MathJax.js')
    assert r.code == 200


async def test_mathjax_conf_handler(jp_fetch):
    r = await jp_fetch('static', 'components', 'MathJax', 'config', 'TeX-AMS-MML_HTMLorMML-full.js')
    assert r.code == 200

    r = await jp_fetch('static', 'components', 'MathJax', 'config', 'Safe.js')
    assert r.code == 200
