from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.core.files.storage import FileSystemStorage

import cv2
from easyocr import Reader
# from PIL import Image
# import io
from textblob import TextBlob
import urllib.request
import numpy as np

# def prepare_image(path):
#     res = Image.open(path)
#     res.thumbnail((400, 400))
#     bio = io.BytesIO()
#     res.save(bio, format="PNG")
#     return bio.getvalue()


def cleanup_text(text):
    # strip out non-ASCII text so we can draw the text on the image
    # using OpenCV
    return "".join([c if ord(c) < 128 or (ord(c) >= 1040 and ord(c) <= 1103) else "" for c in text]).strip()


def text_to_send(text):
    s = ''
    for t in text:
        s += t + '\n'
    return s


def process(url, lang):
    # print('OCR`ing with the following language: {}'.format(lang))
    # image = cv2.imread(path)
    req = urllib.request.urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    image = cv2.imdecode(arr, -1)

    reader = Reader([lang], gpu=True)
    #results = reader.readtext(image)
    results = reader.readtext(url)

    all_text = []

    for (bbox, text, prob) in results:
        if lang != 'ru':
            blob = TextBlob(text)
            text = str(blob.translate(from_lang=lang, to='ru'))

        all_text.append(text)

        # unpack the bounding box
        # (tl, tr, br, bl) = bbox
        # tl = (int(tl[0]), int(tl[1]))
        # tr = (int(tr[0]), int(tr[1]))
        # br = (int(br[0]), int(br[1]))
        # bl = (int(bl[0]), int(bl[1]))

        # cleanup the text and draw the box surrounding the text along
        # with the OCR'd text itself
        # text = cleanup_text(text)
        # cv2.rectangle(image, tl, br, (0, 255, 0), 2)
        # if lang != 'ru':
        #     cv2.putText(image, text, (tl[0], tl[1] - 10),
        #                 cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)

    # show the output image
    # cv2.imwrite('res.png', image)
    # result = prepare_image('res.png')
    res_text = text_to_send(all_text)
    return res_text
    
@api_view(['POST'])
def tr_text(request):
    img_url = request.data.get('img_url')
    # img = request.FILES[0]
    # fs = FileSystemStorage()
    # filename = fs.save(img.name, img)
    # img_url = fs.url(filename)
    img_lang = request.data.get('img_lang')

    if img_url and img_lang:
        text = process(img_url, img_lang)
        response_data = {
            'text': text
        }
        return JsonResponse(response_data)
    else:
        print("Картинка не найдена.")
        return JsonResponse({'error': 'Failed to get the picture.'}, status=400)