#!.venv/bin/python
__author__ = 'Joker Interactive'
__email__ = 'info@jokerinteractive.ru'
import os

# from config import UPLOAD_PATH
from mindsurf import app as application

if __name__ == '__main__':

    # Create upload directory
    # try:
    #    os.mkdir(UPLOAD_PATH)
    # except OSError:
    #    pass
    application.run(port=4444)
