from flask import render_template
from pkg import app

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/pharmacist')
def pharmacist():
    return render_template('pharmacist.html')

@app.route('/investors')
def investors():
    return render_template('investors.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/careers')
def careers():
    return render_template('careers.html')

@app.route('/legal')
def legal():
    return render_template('legal.html')

# Custom Error Handling for Production
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
