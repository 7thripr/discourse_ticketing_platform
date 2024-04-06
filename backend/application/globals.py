# Online Support Ticket Application
# Tushar Supe : 21f1003637
# Vaidehi Agarwal: 21f1003880
# File Info: This file contains global constants and variables.

# --------------------  Imports  --------------------

import os

# --------------------  Code  --------------------

BACKEND_ROOT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
HOST = "127.0.0.1"
PORT = 5000
DEBUG = True
ENV_TYPE = "dev"  # "test"
BASE = f"http://{HOST}:{PORT}"
API_VERSION = "v1"
TOKEN_VALIDITY = 1200*60*60  # seconds
ACCEPTED_IMAGE_EXTENSIONS = ["jpg", "jpeg", "png", "gif"]
PROFILE_PIC_PATH = os.path.join(
    BACKEND_ROOT_PATH, "databases", "images", "profile_pics"
)
TICKET_ATTACHMENTS_PATH = os.path.join(
    BACKEND_ROOT_PATH, "databases", "images", "ticket_attachments"
)
FAQ_ATTACHMENTS_PATH = os.path.join(
    BACKEND_ROOT_PATH, "databases", "images", "faq_attachments"
)

# TEAM 19 - MJ
BASE_DISCOURSE = "https://t19support.cs3001.site"

# TEAM 19 / PB: Discourse API 
DISCOURSE_HEADERS = {
    "Api-Key": "3030e413d91e5c7b3df76b994fe35f75bbf507e3701e7e7375881bc414a1454b",
    "Api-Username": "System"
}

# Mailhog runs at http://127.0.0.1:8025/
SMTP_SERVER_HOST = "127.0.0.1"
SMTP_SERVER_PORT = 1025
SENDER_ADDRESS = "osts_group_14@gmail.com"  # dummy mail and password
SENDER_PASSWORD = "1234"

# --------------------  END  --------------------
