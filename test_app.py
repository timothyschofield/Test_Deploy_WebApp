"""
    How to create a local venv environment

    1) On Debian/Ubuntu systems, you need to install the python3-venv
    package using the following command.
    sudo apt install python3.10-venv
    
    2) Create a venv folder
    python3 -m venv .venv
    At this point you will be asked to select a python interpreter so do so.
    
    3) Activate venv (You will see "(venv)" appesr to the left of the terminal prompt if all goes well)
    source .venv/bin/activate
    
    4) I have installed the dependencies by hand using pip install XXXX
    There is probably some smart method of doing this
    
    5) Generate requirments.txt from project imports
    pip freeze > requirements.txt
    7 dependancies for this small Flask app
    
    Install dependencies in venv from requirments.txt
    pip install -r requirements.txt
     
"""
from flask import Flask, render_template, request

flask_app = Flask(__name__)

@flask_app.route("/", methods=["GET", "POST"])
def index():
    name = None
    # From the Submit button
    if request.method == "POST":
        # Get the name from the form submission
        name = request.form.get("name")
    
    # Render the HTML page and pass the 'name' to it
    return render_template("tim.html", name=name)

if __name__ == "__main__":
    flask_app.run(debug=False)
