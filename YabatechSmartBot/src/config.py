# src/config.py

import os

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Data paths
DATA_DIR = os.path.join(BASE_DIR, 'data')
STUDENT_DATA_PATH = os.path.join(DATA_DIR, 'student_data.csv')
STAFF_INFO_PATH = os.path.join(DATA_DIR, 'staff_info.csv')
SCHOOL_EVENTS_PATH = os.path.join(DATA_DIR, 'school_events.csv')
FAQ_DATA_PATH = os.path.join(DATA_DIR, 'faq_data.csv')
CHAT_LOGS_PATH = os.path.join(DATA_DIR, 'chat_logs.csv')

# Model paths
MODEL_DIR = os.path.join(BASE_DIR, 'model')
NLP_MODEL_PATH = os.path.join(MODEL_DIR, 'nlp_model.pkl')

# Assets paths
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
LOGO_PATH = os.path.join(ASSETS_DIR, 'yabatech_logo.png')

# Constants
APP_TITLE = "Yabatech SmartBot"
WELCOME_MESSAGE = "Welcome to the Yabatech SmartBot! How can I help you today?"
