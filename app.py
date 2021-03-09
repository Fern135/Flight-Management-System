"""
# macOS/Linux
    # You may need to run sudo apt-get install python3-venv first
    python3 -m venv venv

    # Windows
    # You can also use py -3 -m venv .venv
    python -m venv venv

    mac / linux
    source env/bin/activate

    windows 
    .\venv\Scripts\activate
"""
from flask import *
from datetime import timedelta
from os import system, name  # clear the screen
from colorama import *
import datetime
import string
import random
import json

# initiate the flask web framework
app = Flask(__name__)

# region temporary
# key for the session. just made it fun
app.secret_key = b"This is but something of secret value don't you dare try and see this."

# maximum days to keep the session timer
app.permanent_session_lifetime = timedelta(days=30)

# region debugging in terminals
colorama.init(autoreset=True)  # this error doesn't matter it still works fine.
RED = Fore.RED
# endregion


@app.route("/", methods=['POST', 'GET'])
def home():  # home screen
    return render_template("index.html")


# region api section
@app.route('/api/getFlights', methods=['POST', 'GET'])
def getFlights():  # api for getting the flights
    try:
        data = json.dumps(request.data)  # parsing the info via json requests

        print(data)

    except Exception as e:
        log(str(e))
        print(f"error {str(e)}")

# endregion

# region userful functions


def get_time():  # get full 12 hour time
    x = datetime.datetime.now()

    hour = x.strftime("%I")  # hour
    min = x.strftime("%M")  # minute
    AMPM = x.strftime("%p")  # am / pm

    return f"{hour} : {min} : {AMPM}"


def get_Date():  # get full date
    return datetime.datetime.now().strftime("%x")


def log(msg):  # writing a .txt file with the errors in a list
    # make this into an excel file or something more readable and user friendly
    """
        log number being written.
        get the date and time
        and showing the log
    """
    f = open("./err_log/log.txt", "a")
    f.write(
        f"\n________________________________\n" +
        f"      log id: {rnd(1000000)}    \n" +
        f"________________________________\n" +
        f"      date: {get_Date()}      \n" +
        f"________________________________\n" +
        f"      time: {get_time()}      \n" +
        f"________________________________\n" +
        f"      error log: {msg}        \n" +
        f"________________________________\n"
    )
    f.close()

    print("Error logged into log.txt........")


def genRandChar(N):  # generating the random api key and saving it with each user
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))


def rnd(last):  # random number generator for choosing 1
    return random.randint(1, last)


def cls():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# endregion


def run():  # do not delete this
    try:
        app.run(threaded=True, host='0.0.0.0', debug=True)
    except Exception as e:
        log(str(e))  # logging any known errors.
        print(f"error: {str(e)}")

# endregion


if __name__ == '__main__':  # the start of the api
    run()
