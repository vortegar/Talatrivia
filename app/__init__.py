from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    app.config.from_object('config.Config') 

    migrate.init_app(app, db) 
    db.init_app(app)

    from app.models import user, trivia, question, associative_tables

    from routes.rank import rank_bp
    from routes.login import login_bp
    from routes.trivia import trivia_bp
    from routes.register import register_bp
    from routes.dashboard import dashboard_bp
    from routes.assign_trivia import assign_trivia_bp
    from routes.create_trivia import create_trivia_bp
    from routes.dashboard_admin import dashboard_admin_bp
    from routes.create_question import create_question_bp

    app.register_blueprint(rank_bp)    
    app.register_blueprint(login_bp)
    app.register_blueprint(trivia_bp)  
    app.register_blueprint(register_bp)    
    app.register_blueprint(dashboard_bp)  
    app.register_blueprint(assign_trivia_bp)  
    app.register_blueprint(create_trivia_bp)  
    app.register_blueprint(create_question_bp)  
    app.register_blueprint(dashboard_admin_bp) 

    return app



