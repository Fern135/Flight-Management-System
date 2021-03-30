"""
This script runs the Flight_Management application using a development server.
"""

from os import environ
from Flight_Management import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST,PORT,debug=True)
