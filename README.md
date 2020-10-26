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
$ <python> -m virtualenv <env>

$ source /<path>/<to>/<env>/bin/activate (Linux & macOS)
```
or
```
$ \<path>\<to>\<env>\scripts\activate (Windows)
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
or change `"SECRET_KEY"` in `base/settings/base.py` 

Run server:
```
$ python manage.py runserver
```