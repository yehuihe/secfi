# secfi
Secfi auth assignment 



1. Set environment variables

export FLASK_APP=secfi.py
export FLASK_DEBUG=1

2. Dependencies 

pip install -r requirements/dev.txt

3. Migrate Database

flask db init
flask db migrate -m "role users migration"
flask db upgrade

3. Add role and admin

flask shell
Role.insert_roles()
Role.query_all()

r = Role.query.filter_by(name='Administrator').first()
u = User(username='admin', password='admin', role=r)
db.session.add(u)
db.session.commit()

User.query.all()
exit()


API Routes in 
app/api/users.py
app/api/authentication.py

Open Web app please run:

flask run
