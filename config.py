import os
class Config:

  UPLOADED_PHOTOS_DEST ='app/static/photos' 
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wairimu:wairimu12@localhost/wairimu'