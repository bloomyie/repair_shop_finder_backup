from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Use this generated secret key
SECRET_KEY = 'django-insecure-412f3j+3_&+n1qlk9h$y7u4i9u4ex#%2@b@z&h!b5e&(p2h%'
DEBUG = False  # Set to False for production

# Update this line with actual deployment server address and localhost for testing
ALLOWED_HOSTS = [
    'repair-shop-finder-gefipkxmi-hartley-bloomfields-projects.vercel.app', 
    'repair-shop-finder-jtvysirea-hartley-bloomfields-projects.vercel.app', 
    'shopfinder-424119.wn.r.appspot.com', 
    '127.0.0.1', 
    'localhost'
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shops',  # Assuming 'shops' is your app, ensure it's created and configured
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF
