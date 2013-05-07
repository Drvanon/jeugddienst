from bottle import run, route, jinja2_view as view, request
from bottel import post, get
from database import *

session = Session()

@route('/')
@view('home.html')
def home():
    return {}
    
@post('/forum/<forumname>')
def forum_post(forumname):
    if forumname in session.query(Forum).all():
        name = request.forms.get('name')
        reaction = request.forms.get('reaction')
    else:
        return {'error':'That forum does not exist'}