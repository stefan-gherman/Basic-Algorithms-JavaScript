from flask import Flask, redirect, request,render_template, url_for


app = Flask(__name__)

@app.route('/')
def return_home():
    return render_template('home.html')

@app.route('/fizzbuzz')
def return_fizzbuzz():
    return render_template('fizzbuzz.html')

@app.route('/search')
def return_search():
    return render_template('search.html')

if __name__=='__main__':
    app.run(debug=True)