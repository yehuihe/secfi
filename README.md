# secfi
Secfi auth assignment 

## Disclaimer 
I realize that in API design. Use user id as identifiers in routes isn't a good choice as user don't remember their id.
But due to time constrain this is a easy way out. In production I'll switch to username. I also added the password_hash in User route just
for showing purpuses. Of course in real it won't be there.


1. Set environment variables

`export FLASK_APP=secfi.py
export FLASK_DEBUG=1
`

2. Dependencies 

`pip install -r requirements/dev.txt
`

3. Migrate Database

`flask db init
flask db migrate -m "role users migration"
flask db upgrade
`

4. Add role and admin

`flask shell
Role.insert_roles()
Role.query_all()

r = Role.query.filter_by(name='Administrator').first()
u = User(username='admin', password='admin', role=r)
db.session.add(u)
db.session.commit()

User.query.all()
exit()
`

API Routes in:

app/api/users.py
app/api/authentication.py

To use API service:

`flask run
`
Routes:

- Get tokens:
http://127.0.0.1:5000/api/v1/tokens/             GET

- Get users info (only admin or current user):
http://127.0.0.1:5000/api/v1/users/<int:id>      GET

- Create new users (only admin):
http://127.0.0.1:5000/api/v1/users/              POST

- Edit user self (only admin or current user):
http://127.0.0.1:5000/api/v1/users/<int:id>      PUT
Required: username, password
Optional: first_name, last_name

- Self-removal (only current user):
http://127.0.0.1:5000/api/v1/users/              DELETE

### Guide: 
Current api can't design roles. admin can only be added to database in flask shell. All other create new users by admin in API are only to add User.
After adding admin in database. Create a few new users. For example in HTTPie:

http --json --auth admin:admin POST http://127.0.0.1:5000/api/v1/users/ username=johndoe password=cat first_name=John last_name=Doe

Get user
http --json --auth admin:admin GET http://127.0.0.1:5000/api/v1/users/1 

or current user john 2

http --json --auth john:cat GET http://127.0.0.1:5000/api/v1/users/2

To use token access. generate tokens via GET tokens. Copy token then replace username with token and leave password empty. For example:

http --json --auth <token>: GET http://127.0.0.1:5000/api/v1/users/1 

**Get user has password_hash. Which is just for the assignment. Not for real scenario**

There is no inspect all user id currently. so you can view user id in flask shell:

`flask shell
User.query.all()
`
Open Web app please run:

`flask run
`

