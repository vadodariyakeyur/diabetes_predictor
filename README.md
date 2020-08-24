# diabetes_predictor

To run the app, first, you need to set the FLASK_APP environment variable.

To set the environment variable from Windows PowerShell, run

**_(myenv) PS C:\myfirstapp> $env:FLASK_APP = "app.py"_**

From a Windows Command Prompt, run the set command.

**_C:\myfirstapp> set FLASK_APP=app.py_**

To set FLASK_APP environment variable in Linux

**_$ export FLASK_APP=app.py_**

You can then run the application using the flask run in both Windows and Linux.

**_(myenv) PS C:\myfirstapp> flask run_**

**_Serving Flask app "app.py"_**

**_Environment: production_**

**_WARNING: This is a development server. Do not use it in a production deployment._**

**_Use a production WSGI server instead._**

**_Debug mode: off_**

**_App.py __name__ = app_**

**_Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)_**
 
Now, open a web browser and enter the URL http://127.0.0.1:5000/ and you should see the webpage.

To stop the application simply press CTRL+C in the terminal where you started the app.
