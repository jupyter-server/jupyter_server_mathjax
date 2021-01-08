import os
from traitlets import HasTraits, Unicode, Bool, observe, default
from jupyter_server.utils import url_path_join


class MathJaxTraitsMixin(HasTraits):

    enable_mathjax = Bool(
        True,
        config=True,
        help="""Whether to enable MathJax for typesetting math/TeX

        MathJax is the javascript library Jupyter uses to render math/LaTeX. It is
        very large, so you may want to disable it if you have a slow internet
        connection, or for offline use of the notebook.

        When disabled, equations etc. will appear as their untransformed TeX source.
        """,
    )

    @observe("enable_mathjax")
    def _update_enable_mathjax(self, change):
        """set mathjax url to empty if mathjax is disabled"""
        if not change["new"]:
            self.mathjax_url = u""

    mathjax_url = Unicode(
        "",
        config=True,
        help="""A custom url for MathJax.js.
        Should be in the form of a case-sensitive url to MathJax,
        for example:  /static/components/MathJax/MathJax.js
        """,
    )

    @default("mathjax_url")
    def _default_mathjax_url(self):
        if not self.enable_mathjax:
            return u""
        static_url_prefix = self.static_url_prefix
        return url_path_join(static_url_prefix, "components", "MathJax", "MathJax.js")

    @observe("mathjax_url")
    def _update_mathjax_url(self, change):
        new = change["new"]
        if new and not self.enable_mathjax:
            # enable_mathjax=False overrides mathjax_url
            self.mathjax_url = u""
        else:
            self.log.info(_("Using MathJax: %s"), new)

    mathjax_config = Unicode(
        "TeX-AMS-MML_HTMLorMML-full,Safe",
        config=True,
        help=_("""The MathJax.js configuration file that is to be used."""),
    )

    @observe("mathjax_config")
    def _update_mathjax_config(self, change):
        self.log.info(_("Using MathJax configuration file: %s"), change["new"])
