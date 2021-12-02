# pylint: disable=unused-import, wrong-import-position

from flask import Flask

app = Flask(__name__)

import src.routes
