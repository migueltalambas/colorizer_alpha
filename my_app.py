from msilib.schema import File
from urllib import response
from flask import Flask, Response, render_template, request
from colorizer import Colorizer

app = Flask(__name__)
colorizer = Colorizer

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        print(file.filename)
        return render_template('index.html')
    else:
        return render_template('index.html')


@app.route('/display',methods=['GET', 'POST'] )
def run():
    if request.method == 'POST':
        colorizer.processImage(response())
        return render_template('display.html')

if __name__ == '__main__':
    app.run(debug=True, port=4545)