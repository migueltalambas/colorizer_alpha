# from msilib.schema import File
# from urllib import response
# from flask import Flask, Response, render_template, request
# from colorizer import Colorizer

# app = Flask(__name__)
# colorizer = Colorizer

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/submit', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         file = request.files['file']
#         print(file.filename)
#         return render_template('index.html')
#     else:
#         return render_template('index.html')


# @app.route('/display',methods=['GET', 'POST'] )
# def run():
#     if request.method == 'POST':
#         colorizer.processImage(response())
#         return render_template('display.html')

# if __name__ == '__main__':
#     app.run(debug=True, port=4545)

from re import X
from urllib import response
from cv2 import filterHomographyDecompByVisibleRefpoints
from flask import Flask, Response, render_template, request, flash, redirect, url_for, send_from_directory
#from colorizer import Colorizer
from werkzeug.utils import secure_filename
from colorizer import Colorizer
import os


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def colorize_func(img):
    colorizer = Colorizer(use_cuda=True, width = 640, height = 480)
    return colorizer.processImage(img)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template('index.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    print('first ', filename)
    path = "uploads/"
    full = path + filename
    col = colorize_func(full)
    print('second ', col)
    return send_from_directory('output/', filename)
    
    # return colorize_func(full)

if __name__ == '__main__':
    app.run(debug=True, port=4545)