from bottle import run, route, jinja2_view as view, request, default_app
from bottel import post, get
from database import *

session = Session()

@route('/')
@view('home.html')
def home():
    return {}

@get('/forum/<forumname>')
@view('forum.html')
def forum(forumname):
    forum = session.query(Forum).filter_by(title=forumname).first()
    if forum:
        return {'title': forum.title,
                'reactions': forum.reactions
                }
    else:
        return {'error': 'Forum not found.'}

@post('/forum/<forumname>')
def forum_post(forumname):
    forum = session.query(Forum).filter_by(name=forumname).first()
    if forum:
        name = request.forms.get('name')
        reaction = request.forms.get('reaction')
        new_reaction = Reaction(reaction, name)
        session.add(new_reaction)
        session.commit()
    else:
        return {'error':'Forum not found.'}

@get('/poll/<pollname>')
@view('poll.html')
def poll(pollname):
    poll = session.query(Poll).filter_by(title=pollname).first()
    if forum:
        return {'title': poll.title,
                'option1': poll.option1,
                'option2': poll.option2,
                'option3': poll.option3,
                'option4': poll.option4,
                }
    else:
        return {'error': 'Forum not found.'}

@post('/poll/<pollname>')
def poll_post(pollname):
    poll = session.query(Poll).filter_by(name=pollname).first()
    if poll:
        vote = request.forms.get('reaction')
        new_reaction = Reaction(reaction, name)
        session.add(new_reaction)
        session.commit()
    else:
        return {'error':'Forum not found.'}

if __name___ == '__main__': run(debug=True)
else: application = default_app()