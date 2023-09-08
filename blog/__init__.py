from flask import Flask, render_template
from .config.variables import SECRET_KEY

def create_app():
    app = Flask(__name__)

    # CONFIG
    app.config["SECRET_KEY"] = SECRET_KEY

    # BLUEPRINT
    from .views.admin_auth import admin
    app.register_blueprint(admin, url_prefix="/owner")

    # ERROR ROUTES

    # 404 - ERROR
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('admin/error-404.html')
    
    # 500 - ERROR
    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('admin/error-500.html')
    
    return app