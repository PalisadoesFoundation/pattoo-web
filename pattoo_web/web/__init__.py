"""Initialize the PATTOO_WEBD module."""

# Import PIP3 libraries
from flask import Flask

# Define the global URL prefix
from pattoo_shared.constants import PATTOO_WEB_SITE_PREFIX

# Import PATTOO_WEBD Blueprints
from pattoo_web.web.home import PATTOO_WEB_HOME

# Setup flask
PATTOO_WEBD = Flask(__name__)

# Register Blueprints
PATTOO_WEBD.register_blueprint(
    PATTOO_WEB_HOME, url_prefix=PATTOO_WEB_SITE_PREFIX)
