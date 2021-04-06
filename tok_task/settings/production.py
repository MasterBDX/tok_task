
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'p6h2t2+i+2fh)8yfu%_d_#p17lopc@iwa4d*-rln^fi#p1*h_b'

BASE_URL = 'http://website-name.com/'

DEBUG = False

ALLOWED_HOSTS = ['*']



STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']



# DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
# DROPBOX_OAUTH2_TOKEN = os.environ.get('DROPBOX_OAUTH2_TOKEN')
# DROPBOX_ROOT_PATH = ''

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
