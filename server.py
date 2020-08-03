from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/about.html')
def about_page():
    return render_template('about.html')

@app.route('/components.html')
def components_page():
    return render_template('components.html')

@app.route('/contact.html')
def contact_page():
    return render_template('contact.html')

