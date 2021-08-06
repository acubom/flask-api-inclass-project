import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Give access to the project in any OS we find ourselves in here.
# Allows outside files/folders to be added to the project from the base directory.

class Config:
    """
    Set configuration variables for our Flask app here
    Eventually will use hidden varible items - but for now, we'll leave them exposed in config
    """
    SECRET_KEY="You will never guess..."
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL')
    # Decreases unnessary optput in terminal
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
