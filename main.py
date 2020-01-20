from flask import Flask, redirect, request,render_template, url_for


app = Flask(__name__)

@app.route('/')
def return_home():
    return render_template('fizzbuzz.html')
if __name__=='__main__':
    app.run(debug=True)