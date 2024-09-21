import os

from company.repository import company_repository
from core.repository import contact_repository
from project.repository import project_repository
from service.repository import service_repository

# --- Site Data ---
SITEURL = os.getenv("SITEURL", default="https://inperium.eu")
AUTHOR = "Lukasz Zmudzinski"
SITENAME = "INPERIUM"
TIMEZONE = "Europe/Warsaw"
DEFAULT_LANG = "en"

# --- Pelican Paths and Settings ---
PATH = "content"
THEME = "themes/core"
THEME_STATIC_DIR = "theme"
DEFAULT_PAGINATION = False
DELETE_OUTPUT_DIRECTORY = True
STATIC_PATHS = ["images", "extra/CNAME"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}

# --- Feed Generation ---
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# --- Site Data ---
SITE_DATA = {
    "contact": contact_repository.get_contact(),
    "services": service_repository.get_services(),
    "projects": project_repository.get_projects(),
    "companies": company_repository.get_companies(),
}
