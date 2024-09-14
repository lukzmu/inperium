import os

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
    "contact": {
        "email": "hello@inperium.eu",
        "vat": "PL7393659738",
        "regon": "380660414",
    },
    "projects": [
        {
            "name": "IoT Emergency Lightning System",
            "icon": "iot_lightning.png",
        },
        {
            "name": "Medical Knowledge Base",
            "icon": "medical_knowledge_base.png",
        },
        {
            "name": "Airport A-SMGCS System",
            "icon": "asmgcs.png",
        },
        {
            "name": "Analytics Dashboard for ML",
            "icon": "dashboard_ml.png",
        },
        {
            "name": "Online RPG UI Enhancement",
            "icon": "rpg.png",
        },
        {
            "name": "Smart Car Fleet Manager",
            "icon": "car_fleet.png",
        },
        {
            "name": "SNOMED Code Library",
            "icon": "snomed.png",
        },
        {
            "name": "AR Furniture Builder",
            "icon": "ar_furniture.png",
        },
        {
            "name": "Fintech Travel Portal",
            "icon": "travel.png",
        },
        {
            "name": "IoT City Heating Platform",
            "icon": "heating.png",
        },
        {
            "name": "Robotics Path Planning",
            "icon": "path_planning.png",
        },
    ],
    "companies": [
        {
            "name": "Infermedica",
            "icon": "infermedica.svg",
        },
        {
            "name": "Merixstudio",
            "icon": "merixstudio.svg",
        },
        {
            "name": "Microsoft",
            "icon": "microsoft.svg",
        },
        {
            "name": "AP-Tech",
            "icon": "aptech.svg",
        },
        {
            "name": "Treesat",
            "icon": "treesat.svg",
        },
    ],
}
