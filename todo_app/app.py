from flask import Flask

app = Flask(__name__)

# Import and register the todo blueprint
from todo_app.routes.todo_routes import todo_bp
app.register_blueprint(todo_bp, url_prefix='/api')

# Configurations, routes, and other application setup will go here

if __name__ == '__main__':
    app.run(debug=True)
