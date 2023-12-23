from django import forms

class TranslateForm(forms.Form):
    source_lang = forms.ChoiceField(choices=[
        ('en', 'en'),
        ('de', 'de'),
        ('ru', 'ru'),
        ('es', 'es')
        ], label='Язык текста:')
    text = forms.CharField(label='Текст:', widget=forms.Textarea())
    dest_lang = forms.ChoiceField(choices=[
        ('ru', 'ru'),
        ('en', 'en'),
        ('de', 'de'),
        ('es', 'es')
        ], label='Язык перевода:')