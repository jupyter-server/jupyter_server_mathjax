import os

from jupyter_server.base.handlers import FileFindHandler

STATIC_ASSETS_PATH = os.path.join(os.path.dirname(__file__), 'static')

def _jupyter_server_extension_points():
    return [
        {
            "module": "jupyter_server_mathjax",
        },
    ]

def _load_jupyter_server_extension(serverapp):
    static_url_prefix = serverapp.static_url_prefix

    serverapp.handlers.append(
        (static_url_prefix + r"/components/MathJax/(.*)", FileFindHandler, {
            'path': STATIC_ASSETS_PATH,
        })
    )

