# 09C40
## Development environment
Clone project to your local machine:
```
$ git clone https://github.com/plus1349/09C40
```
Proceed to project location:
```
$ cd /<path>/<to>/09C40/
```

Create and activate a virtual environment:
```
$ <python> -m virtualenv <venv>

$ source /<path>/<to>/<venv>/bin/activate (Linux & macOS)
```
or
```
$ \<path>\<to>\<venv>\scripts\activate (Windows)
```
Install requirements:
```
$ pip install -r requirements.txt
```
Use `os` module to set `"SECRET_KEY"` environment variable, example:
```python
from os import environ

environ.setdefault("SECRET_KEY", "<secret key>")
```
or define `"SECRET_KEY"` constant in `base/settings/dev.py` 

Run server:
```
$ python manage.py runserver
```