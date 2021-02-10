
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, render_template, request
import os
from flask_uploads import UploadSet, IMAGES
from PIL import Image
import pytesseract
import just

# path for current location
project_dir = os.path.dirname(os.path.abspath(__file__))
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')
photos = UploadSet('photos', IMAGES)

app.config['DEBUG'] = True
app.config["ALLOWED_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF", "PDF"]
app.config['UPLOAD_FOLDER'] = 'images'
app.config['UPLOAD_FOLDER'] = 'pdf'


# class declaration for image to text conversion

class GetText(object):

    def __init__(self, file):
        self.file = pytesseract.image_to_string(Image.open(project_dir + '/images/' + file))


# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         if 'photo' not in request.files:
#             return 'There is no photo in form'
#         name = request.form['img-name'] + '.png'
#
#         photo = request.files['photo']
#         path = os.path.join(app.config['UPLOAD_FOLDER'], name)
#         photo.save(path)
#
#         # text = just.GetText(name)
#         text = GetText(name)
#         return text.file
#     return render_template('index.html')


@app.route('/ocr', methods=['GET', 'POST'])
def pdf_home():
    text = None
    if request.method == 'POST':
        if 'photo' not in request.files:
            return 'There is no photo in form'
        name = request.form['img-name'] + '.pdf'
        photo = request.files['photo']

        print("request.files['photo']", photo)
        path = os.path.join('pdf', name)

        photo.save(path)
        language_value = request.form['dropdown']
        pdf_img_value = request.form['pdf_img']
        img_value = True
        if pdf_img_value == "pdf_to_img":
            text = just.pdf_to_image(path, language_value)
            img_value = False
        else:
            text = just.GetText(path, language_value)
            img_value = True

        return render_template('pdf_text.html', foobar=text, img_value=img_value)
        # print(type(photo))
    return render_template('index.html')


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    app.run()
