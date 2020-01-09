"""Initialize the PATTOO_WEBD module."""

# Import PIP3 libraries
from flask import Flask, url_for

# Define the global URL prefix
from pattoo_shared.constants import PATTOO_WEB_SITE_PREFIX
from pattoo_web.constants import FOLDER_WEB_STATIC, FOLDER_WEB_TEMPLATE

# Import PATTOO_WEBD Blueprints
from pattoo_web.web.home import PATTOO_WEB_HOME
from pattoo_web.web.chart import PATTOO_WEB_CHART
from pattoo_web.web.status import PATTOO_WEB_STATUS
from pattoo_web.web.agent import PATTOO_WEB_AGENT

# Setup flask
PATTOO_WEBD = Flask(
    __name__,
    static_url_path='{}/static'.format(PATTOO_WEB_SITE_PREFIX),
    static_folder=FOLDER_WEB_STATIC,
    template_folder=FOLDER_WEB_TEMPLATE
)

# Register Blueprints
PATTOO_WEBD.register_blueprint(
    PATTOO_WEB_HOME, url_prefix=PATTOO_WEB_SITE_PREFIX)
PATTOO_WEBD.register_blueprint(
    PATTOO_WEB_CHART, url_prefix='{}/chart'.format(PATTOO_WEB_SITE_PREFIX))
PATTOO_WEBD.register_blueprint(
    PATTOO_WEB_STATUS, url_prefix='{}/status'.format(PATTOO_WEB_SITE_PREFIX))
PATTOO_WEBD.register_blueprint(
    PATTOO_WEB_AGENT, url_prefix='{}/agent'.format(PATTOO_WEB_SITE_PREFIX))

# Function to easily find your assests
PATTOO_WEBD.jinja_env.globals['static'] = (
    lambda filename: url_for(
        'static', filename=filename)
)


@PATTOO_WEBD.context_processor
def inject():
    """Inject global variables for use by templates.

    Args:
        None

    Returns:
        HTML

    """
    # Return
    return dict(
        url_home=PATTOO_WEB_SITE_PREFIX,
        url_static='{}/static'.format(PATTOO_WEB_SITE_PREFIX))
