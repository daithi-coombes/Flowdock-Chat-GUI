flow-chat-py
============

Flowdock Chat built in Python (2.7)

Uses pycurl to connect to flowdock and open a stream.
Threading is used for streaming and pushing data.

usage
=====
Create a file called 'settings.py' with the following variables:
```python
    DEBUG = 1
    API_TOKEN = "Api token for flow"
    USER = "Login username"    #this is the user email address (user for logging in)
    USER_NAME = "Display Name"     #the display name for the user
    PASS = "Login Password"
```
save and then run:
	python __init__.py