import os
from flask import Flask
app=Flask(__name__)

@app.route("/")
def main():
    return "Welcome Dhari"

@app.route("/how are you")
def hello():
    return "I am Good how about you?"

if __name__== "__main__":
    app.run()