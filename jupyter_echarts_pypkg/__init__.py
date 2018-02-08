# flake8: noqa
import os

from jupyter_echarts_pypkg._version import __version__
from jupyter_echarts_pypkg._version import __author__
from lml.plugin import PluginInfoChain, PluginInfo
from pyecharts.js_extensions import JsExtension


@PluginInfo('pyecharts_js_extension', tags=['core'])
class JupyterEcharts(JsExtension):
    def __init__(self):
        __package_path__ = os.path.dirname(__file__)
        __registry_json__ = os.path.join(
            __package_path__, "resources")
        super(JupyterEcharts, self).__init__(__registry_json__)

