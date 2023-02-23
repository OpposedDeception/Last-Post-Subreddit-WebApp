from flask import Flask, render_template
import praw

app = Flask(__name__)

# Get necessary data from the Developer Settings in the Reddit
reddit = praw.Reddit(
client_id='your client id',
client_secret='your client secret',
user_agent='your user agent',
username='your nickname',
password='your password'
)

def post():
    subreddit = reddit.subreddit("androidroot")
    posts = subreddit.new(limit=14)
    return list(posts)


@app.route("/")
def index():
    posts = post()
    return render_template("index.html", posts=posts)
    
if __name__ == "__main__":
    app.run(debug=True)
