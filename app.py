from flask import *
from app import create_app
from app.extensions import db

app = create_app()

# with app.app_context():
#     print('Creating Database And Tables')
#     db.create_all()
#     print('Created Database and tablesss')

if __name__ == '__main__':
    app.run(debug=True)



