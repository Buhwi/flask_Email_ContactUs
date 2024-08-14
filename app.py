from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

app = Flask(__name__)

# 환경 변수에서 값을 가져옵니다.
app.secret_key = os.urandom(24)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = (os.getenv('MAIL_USERNAME'))

mail = Mail(app)

@app.route('/')
def index():
    return render_template('contact.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(f'Contact Form Submission from {name}',
                      recipients=[os.getenv('MAIL_USERNAME')])  # 본인의 이메일로 전송
        msg.body = f"""
        Name: {name}
        Email: {email}
        Message: {message}
        """
        
        try:
            mail.send(msg)
            flash('성공적으로 메세지를 전송하였습니다.', 'success')
        except Exception as e:
            flash(f'메세지 전송을 실패하였습니다. Error: {e}', 'danger')

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
