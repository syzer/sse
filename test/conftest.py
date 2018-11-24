from dotenv import load_dotenv
import django
import os


basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
envfile = os.path.join(basedir, '.env.testing')
load_dotenv(envfile)

django.setup()
