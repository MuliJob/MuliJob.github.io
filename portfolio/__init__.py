from flask import Flask, render_template

app=Flask(__name__, template_folder="template")
@app.route('/')
def home_page():
    return render_template('index.html')