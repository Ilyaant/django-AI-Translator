# django-AI-Translator
Веб-приложение на Django, предоставляющее функционал машинного перевода текста. Пользователь указывает язык оригинала, текст для перевода и язык, на который нужно перевести текст; ответом приложения является переведенный текст.
## API приложения
API приложения доступно по адресу http://127.0.0.1:8000/api/trText/ и принимает следующие аргументы:
* `slang` - язык оригинала;
* `text` - текст для перевода;
* `dlang` - язык, на который нужно перевести текст;
Пример запроса:
```json
{
  "slang": "en",
  "text": "Reading practice to help you understand long, complex texts about a wide variety of topics, some of which may be unfamiliar. Texts include specialised articles, biographies and summaries.",
  "dlang": "ru"
}
```
Пример ответа:
```json
{
  "text": "Практика чтения, чтобы помочь вам понять долгие, сложные тексты о самых разных темах, некоторые из которых могут быть незнакомыми. Тексты включают специализированные статьи, биографии и резюме."
}
```
## Инструкция по установке и запуску
1. Установить Docker и Docker Compose.
2. Клонировать репозиторий: `git clone https://github.com/Ilyaant/django-AI-Translator.git`.
3. Перейти в директорию, содержащую файлы Docker: `cd django-AI-Translator/docker`.
4. Выполнить команду: `docker-compose up -d`.
5. API будет доступно по адресу `http://127.0.0.1:8000/api/trText/`.
## Postman-коллекция запросов
Ссылка на Postman-коллекцию с примером POST-запроса к API: https://api.postman.com/collections/15056214-aeaa0494-fa63-4d41-a288-5dbe1ec4de39?access_key=PMAT-01HJ60DRQM75QTYTWESGX158NT
