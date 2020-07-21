# tellme
0. Create `django_project` folder
1. `cd django_project` and `touch requirements.txt`
2. `echo "Django==3.0.8" >> requirements.txt`
3. `python3 -m venv env`
4. `source env/bin/activate`
5. `pip install -r requirements.txt`
COMMIT
6. `django-admin startproject mysite`
7. `cd mysite` and `python manage.py startapp polls`
COMMIT
8. Start app `python manage.py runserver`  
- It created `db.sqlite3`  
- It says ```You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.```

9. Go to `models.py`  
- Creare Question and Choice models

10. Stop app on the terminal (ctrl+c) and run `python manage.py makemigrations polls`  
- It says `No installed app with label 'polls'.`  
- Go to `mysite/settings.py` and add `polls` in INSTALLED_APPS and run the command again
11. Run `python manage.py migrate`. It created `polls/migrations` folder
12. Populate the DB  
- Run `python manage.py shell`, it opens django shell
- `import django` 
- `django.setup()`
- `from polls.models import Question, Choice`
- `Question.objects.all()` This prints <QuerySet []> which means no data
- `from django.utils import timezone`
- `q= Question(q_title = "Best gift for a gamer?",q_text="I am looking for cool gift ideas for my fiance who likes video games.",  q_date=timezone.now())`
- Save the question `q.save()`
- Run again `Question.objects.all()` and it says <QuerySet [<Question: Question object (1)>]>
- Go to `models.py` and add `__str__` method into the Question class
- `exit()` and do `python manage.py shell` again. 
- `import django` and `django.setup()` and `from polls.models import Question, Choice` and now it shows the question that I added.

- Add choices `q=Question.objects.get(pk=1)` and then `q.choice_set.create(choice_test = "bob", votes=0`. Add a few more choices like this
- `q.save()` and `exit`

13. Access admin tool, we need login 
- `python manage.py createsuperuser` and enter username, email adress and password
-Start the app again `python manage.py  runserver` and go to `http://127.0.0.1:8000/admin`. It shows users and groups, we want to see questions and choices
- Go to `admin.py`, register Question and Choice. Check the localhost. Click on Question, it shows the question I added. Add Question on dashboard. Then add Choice, it ask for a question to link

14. URLS: show some content. Add `polls/` path. Also create a `urls.py` file under `polls` folder. Add urls patterns there as well
- Go to `views.py` and add HTTP responses and run the server again.

15. Views
- Add new functions to `view.py` like index function
- Go to `polls/urls.py` add paths for the newly created functions detail, results, vote and then go check localhost `http://127.0.0.1:8000/polls/1/results`
- import Question and get quetions from the db in `index` function and return as a http response

16. [Templates](https://docs.djangoproject.com/en/3.0/topics/templates/)  
A Django project can be configured with one or several template engines (or even zero if you don’t use templates). Django ships built-in backends for its own template system, creatively called the Django template language (DTL), and for the popular alternative Jinja2.
- Add `templates/polls` folder under `polls` directory
There can be many index.html if you have multiple apps. So we use a folder for each app
- Add and html file called index.html and add some basic tags head,body etc
- Add DTL tags (Tags provide arbitrary logic in the rendering process like if statements or loops. Tags are surrounded by {% and %})

16. Go to `views.py` and import loader 
- Add template in index function `template = loader.get_template('polls/index.html')` and the context
- Return template.render
- Run server
OR
- use django.shortcuts.render and pass request, template path and context

17. Detail View - `views.py`  
- Get question by id in `detail` function
- render and return detail.html (which is not created yet)
- Create `detail.html` under `templates/polls` and add DTL for the choices
- This is nice and all however, we have a lot of html pages.  We need a base.html for all.
- Add a new html file called `base.html` and the `main_content` block
- Go to `detail.html` and remove head, body, etc and extend the base html and add the `block`. 
- Do the same thing for `index.html` and extend base
- Refresh, there should be no changes

Daha bitmedi.
- Add a new html file `footer.html` and add a simple text
- Go to `base.html` and include this footer. Now every page has a footer

18. Go to `views.py` and import get_object_or_404
- Add this into `detail` function
- Check localhost, it says 404 when you request http://127.0.0.1:8000/polls/5/

19. Creating a Form 
- Enable us to vote
- Go to `index.html` and use url tags (more SEO friendly) `{% url "detail" question.id %}` in the href.
- We have to use namespace. Go to `mysite/urls.py` and add `namespace="polls"` into polls path
- Come back to `index.html` and add `polls:` into url tag
- Go to `detail.html` add error message. Then add a form with action. You need `csrf_token` 
- Go to `views.py` and modify the results and vote functions
- Create an html file called `results.html` which should extend base.html

20. CSS
static files
- Create `static/polls` folder
- Create `style.css` file and styles for `li` and `a`
- Go to `base.html` and add `{% load static %}` at the top and add a link in the head tag
- Check localhost, the style shoud be changed
- Now add a background image. Create a `images` folder under `static/polls`. Put an image inside.
- Go to `style.css` and add `body`. Now check localhost

21. Add Bootstrap
FW for responsive, mobile first projects on the web
You have to download etc. I dont wanna do that. But if you want to, download bootstap and add the folder under static/polls