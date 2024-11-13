from flask import Flask, render_template, session, g
from flask_migrate import Migrate
from exts import db
import config
from blueprints.auth import bp
from models import UserModel

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(bp)


@app.route('/')
def about():  # put application's code here
    return render_template('index.html')


@app.route('/about')
def index():
    return render_template('about.html')


@app.route('/blogpost')
def blogpost():
    return render_template('blog-post.html')
    # return render_template('tmp.html')


# @app.route('/test')
# def test():
#     return render_template('base.html')

@app.route('/tmp')
def tmp():
    return render_template('publish.html')


@app.before_request
def my_before_request():
    user_id = session.get('user_id')
    if user_id:
        user = UserModel.query.get(user_id)
        setattr(g, 'user', user)
    else:
        setattr(g, 'user', None)


@app.context_processor
def my_context_processor():
    return {'user': g.user}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
