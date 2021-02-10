from wand.image import Image as wi
import os
from PIL import Image
import pytesseract

proj_dir = os.path.dirname(os.path.abspath(__file__))
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pdf_file_content = []


def pdf_to_image(path, language_value):
    outputDir = 'ima/'
    print('pdf_file path', path)
    print('pdf_file path', path)
    PDF_file = wi(filename=path, resolution=400)
    ImageSequence = 0

    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    for img in PDF_file.sequence:
        Image1 = wi(image=img)
        f = 'ima/Image' + language_value + str(ImageSequence) + ".jpg"
        Image1.save(filename=f)
        pdf_file_content.append(GetText(f, language_value))
        ImageSequence += 1

    print('-----------------------------------')
    print('pdf_file_content:', pdf_file_content)
    return pdf_file_content


def GetText(file_name, language_value):
    file = pytesseract.image_to_string(Image.open(proj_dir + '/' + file_name), lang=language_value)
    print("file content:", file)
    return file



