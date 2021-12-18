# newsrater

`pipenv shell` will run the backend virtual environment, assuming you are in the *django* root directory

use `pipenv install ____` to install a new package, or just `pipenv install` if running on a new system

also, for future reference: include .venv and .env in `.gitignore`



from the mysite directory, run `python manage.py shell` to open your model's API CLI
- use my_obj.choice_set.all() to grab associated options from the related (via SQL) object set

from the mysite directory, run `python manage.py runserver` to run the server
- navigate to http://127.0.0.1:8000/admin
