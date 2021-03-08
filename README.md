# FLASK API 

Implemented Basics of Flask API



# Technologies used
. Python3 - A programming language that lets you work more quickly (The universe loves speed!).
. Flask - A microframework for Python based on Werkzeug, Jinja 2 and good intentions
. Virtualenv - A tool to create isolated virtual environments


## Installation / Usage
* If you wish to run your own build, first ensure you have python3 globally installed in your computer. If not, you can get python3 [here](https://www.python.org).
* After this, ensure you have installed virtualenv globally as well. If not, run this:
    ```
        $ pip install virtualenv
    ```
* Git clone this repo to your PC


* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```
        $ cd <folder-name>
        ```

    2. Create and fire up your virtual environment in python3:
        ```
        $ virtualenv -p python3 venv
        $ pip install autoenv
        ```

* #### Environment Variables
    Create a .env file and add the following:
    ```
    source venv/bin/activate
    export SECRET="some-very-long-string-of-random-characters-CHANGE-TO-YOUR-LIKING"
    export APP_SETTINGS="development"
    ```

    Save the file. CD out of the directory and back in. `Autoenv` will automagically set the variables.
    We've now kept sensitive info from the outside world! 😄

* #### Install your requirements
    ```
    (venv)$ pip install -r requirements.txt
    ```


* #### Running It
    On your terminal, run the server using this one simple command:
    ```
    (venv)$ python app.py
    ```
    You can now access the app on your local browser by using
    ```
    http://localhost:5000/
    ```

