from os import environ
from dotenv import load_dotenv

load_dotenv()

config = {
  "FLASK_ENV": environ.get('FLASK_ENV')
  if environ.get('FLASK_ENV')
  else 'development',
  'PORT': environ.get('PORT') if environ.get('PORT') else 7000,
}
