from app import app, db
import os
from app.models import User, Post

if __name__=="__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 4444)))

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}