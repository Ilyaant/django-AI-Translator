from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .forms import TranslateForm

from textblob import TextBlob
    
@api_view(['POST'])
def tr_text(request):
    rslang = request.data.get('slang')
    rtext = request.data.get('text')
    rdlang = request.data.get('dlang')
    
    if rtext and rdlang and rslang:
        blob = TextBlob(rtext)
        text = blob.translate(from_lang=rslang, to=rdlang)
        response_data = {
            'text': str(text)
        }
        return JsonResponse(response_data)
    else:
        print("Ошибка, не указан один из параметров.")
        return JsonResponse({'error': 'Inappropriate parameters.'}, status=400)
    
def translator(request):
    if request.method == 'POST':
        form = TranslateForm(request.POST)
        if form.is_valid():
            rslang = form.cleaned_data['source_lang']
            rtext = form.cleaned_data['text']
            rdlang = form.cleaned_data['dest_lang']
            blob = TextBlob(rtext)
            text = blob.translate(from_lang=rslang, to=rdlang)
            messages.success(request, '{}'.format(text))

    form = TranslateForm()
    return render(request, 'aitranslate/tr_form.html', {'form': form})