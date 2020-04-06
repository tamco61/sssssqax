from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    db_session.global_init("db/mars_explorer.sqlite")
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    user = session.query(User).all()
    team = [i.team_leader for i in jobs]
    n = 0
    lst = list()
    for i in user:
        if i.id == team[n]:
            lst.append((i.surname, i.name))
            n += 1
            if n == len(team):
                break

    return render_template('index.html', job=[i.job for i in jobs], team_lead=lst, id=[i.id for i in jobs], dur=[i.work_size for i in jobs], lst=[i.collaborators for i in jobs], finish=[i.is_finished for i in jobs])



def main():
    app.run(port=8080, host='127.0.0.1')

if __name__ == '__main__':
    main()