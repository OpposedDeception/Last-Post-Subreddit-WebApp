# SubredditAPI
The simple websites that shows posts from r/androidroot

# Installation

You need to install Flask framework and PRAW API
to make it work without issues.

<img src="https://www.kindpng.com/picc/m/188-1882416_flask-python-logo-hd-png-download.png" height="200" width="300"/>

Type in the command prompt this:

`pip install flask`

Then we need to instal PRAW API library.

<img src="https://i.imgur.io/LYcDAGm_d.webp?maxwidth=640&shape=thumb&fidelity=medium" height="160" width="320"/>

`pip install praw`

## Preparing the API
You need to create and separate folders and files like this.
```
___src folder___
   __init__.py
   api.py
   ___templates___
   index.html
   style.css
```

## Running the API
After that, open your command prompt again and write:
`python3 api.py`

It should output like this:
```
* Serving Flask app 'api'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```
