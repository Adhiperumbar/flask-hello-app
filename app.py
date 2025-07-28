from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/hello/<name>')
def hello(name):
    return f'Hello,{name}! Welcome to Flask'
if __name__=='__main__':
    print("My first flask app")
    print("App created successfully")
    app.run(debug=True)