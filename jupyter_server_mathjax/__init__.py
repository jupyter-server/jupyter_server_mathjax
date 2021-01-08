import os

from jupyter_server.base.handlers import FileFindHandler
from jupyter_server.utils import url_path_join

STATIC_ASSETS_PATH = os.path.join(os.path.dirname(__file__), 'static')

def _jupyter_server_extension_points():
    return [
        {
            "module": "jupyter_server_mathjax",
        },
    ]

def _load_jupyter_server_extension(serverapp):
    static_url_prefix = serverapp.web_app.settings['static_url_prefix']

    serverapp.web_app.add_handlers('.*$', [
        (url_path_join(static_url_prefix, r"components/MathJax/(.*)"), FileFindHandler, {
            'path': STATIC_ASSETS_PATH,
        })
    ])
