from flask import Flask, render_template, request
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
    for post in subreddit.new(limit=1):
        elements = [post.selftext, post.shortlink]
    return elements


@app.route("/", methods=["GET"])
def index():
    posts = post()
    if request.method == "GET":
      return render_template("index.html", posts=posts)
    
if __name__ == "__main__":
    app.run(debug=True)
