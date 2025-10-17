#Radhey 
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "26704085"))
API_HASH = environ.get("API_HASH", "f150646c78f09b4f88bef191a22539c0")
BOT_TOKEN = environ.get("BOT_TOKEN", "8438567514:AAHDHeyMy72S-Nra2HPDXLDLuNcWh8gOEDk")

OWNER = int(environ.get("OWNER", "7640198485"))
CREDIT = environ.get("CREDIT", "7640198485")

TOTAL_USER = os.environ.get('TOTAL_USERS', '').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

