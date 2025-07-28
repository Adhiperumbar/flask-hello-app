from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        message=request.form['message']
        return render_template('thankyou.html',name=name,message=message)
if __name__=='__main__':
    print("My first flask app")
    print("App created successfully")
    app.run(debug=True)