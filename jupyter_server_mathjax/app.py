# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from pathlib import Path
from traitlets import default, observe, Unicode

from tornado.web import RedirectHandler

from jupyter_server.extension.application import ExtensionApp
from jupyter_server.utils import url_path_join
from jupyter_server.transutils import _


STATIC_ASSETS_PATH = Path(__file__).parent / "static"


class DeprecatedRedirectHandler(RedirectHandler):
    def get(self, *args, **kwargs):
        import warnings

        warnings.warn(
            "Redirecting old Notebook MathJax URL to new one. This will be removed in a future release.",
            PendingDeprecationWarning,
        )
        super().get(*args, **kwargs)


class MathJaxExtension(ExtensionApp):

    name = "jupyter_server_mathjax"

    # By listing the path to the assets here, jupyter_server
    # automatically creates a static file handler at
    # /static/jupyter_server_mathjax/...
    static_paths = [str(STATIC_ASSETS_PATH)]

    mathjax_config = Unicode(
        "TeX-AMS-MML_HTMLorMML-full,Safe",
        config=True,
        help=_("""The MathJax.js configuration file that is to be used."""),
    )

    @observe("mathjax_config")
    def _update_mathjax_config(self, change):
        self.log.info(_("Using MathJax configuration file: %s"), change["new"])

    def initialize_settings(self):
        # Add settings specific to this extension to the
        # tornado webapp settings.
        self.settings.update({
            "mathjax_config": self.mathjax_config,
            "mathjax_url": "/static/jupyter_server_mathjax/MathJax.js"
        })

    def initialize_handlers(self):
        webapp = self.serverapp.web_app
        base_url = self.serverapp.base_url
        host_pattern = ".*$"

        # Add a deprecated redirect for all MathJax paths from the classic
        # notebook to the static endpoint created for this extension.
        webapp.add_handlers(
            host_pattern,
            [
                (
                    url_path_join(base_url, "/static/components/MathJax/(.*)"),
                    DeprecatedRedirectHandler,
                    {
                        "url": url_path_join(
                            self.static_url_prefix, "/{0}"  # {0} = group 0 in url path
                        )
                    },
                )
            ],
        )
