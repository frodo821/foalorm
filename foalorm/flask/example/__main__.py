from .views import *
from .app import app

if __name__ == '__main__':
    db.bind(**app.config['FOALORM'])
    db.generate_mapping(create_tables=True)
    app.run()
