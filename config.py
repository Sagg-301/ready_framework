from dotenv import load_dotenv
import os

load_dotenv()

# Statement for enabling the development environment
DEBUG = os.getenv("DEBUG", False) in (True, 'True')

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = "postgres://{0}:{1}@{2}:{3}/{4}".format(os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), os.getenv("DB_HOST"), os.getenv("DB_PORT"), os.getenv("DB_NAME"))
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = False

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = os.getenv("SECRET_KEY")

DROP_DB = os.getenv("DROP_DB", False) in (True, 'True')

ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS")

TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_TOKEN = os.getenv('TWILIO_TOKEN')
TWILIO_PHONE = os.getenv('TWILIO_PHONE')

MAIL_SERVER = os.getenv('MAIL_SERVER')
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', False) in (True, 'True')
MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', False) in (True, 'True')
MAIL_DEBUG = os.getenv('MAIL_DEBUG', False) in (True, 'True')

LANGUAGES = {
    'es': 'Spanish',
}