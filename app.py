from flask import Flask
from flask_mail import Mail
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

# Flask-Mail 초기화
mail = Mail()

def create_app():
    # Flask 애플리케이션 생성 및 설정 불러오기
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Flask-Mail 초기화
    mail.init_app(app)

    # 블루프린트 등록
    from routes import main_bp
    app.register_blueprint(main_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
