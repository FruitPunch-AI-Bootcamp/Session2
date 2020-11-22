"""
This script runs the FPAI_EDA_GRP1 application using a development server.
"""

from os import environ
from FPAI_EDA_GRP1 import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
