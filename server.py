from bottle import run, route, jinja2_view as view, request, default_app
from bottle import post, get, static_file, abort
from database import *

session = Session()

@route('/')
@view('home.html')
def home():
    return {'fora': session.query(Forum).all(), 
            'polls': session.query(Poll).all(),
    }

@get('/forum/<forumname>')
@view('forum.html')
def forum(forumname):
    forum = session.query(Forum).filter_by(url=forumname).first()
    if forum:
        return {'forum':forum}
    else:
        abort(404, 'Forum not found.')

@post('/forum/<forumname>')
def forum_post(forumname):
    forum = session.query(Forum).filter_by(url=forumname).first()
    if forum:
        name = request.forms.get('name')
        content = request.forms.get('reaction')
        new_reaction = Reaction(content, name, forum)
        session.add(new_reaction)
        session.commit()
    else:
        abort(404, 'Forum not found.')

@get('/poll/<pollname>')
@view('poll.html')
def poll(pollname):
    poll = session.query(Poll).filter_by(url=pollname).first()
    if forum:
        return {'poll': poll}
    else:
        abort(404, 'Poll not found.')

@post('/poll/<pollname>')
def poll_post(pollname):
    poll = session.query(Poll).filter_by(url=pollname).first()
    if poll:
        vote = request.forms.get('Poll')
        new_vote= Vote(vote, poll)
        session.add(new_vote)
        session.commit()
    else:
        abort(404, 'Poll not found.')
        
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

if __name__ == '__main__': run(debug=True)
else: application = default_app()