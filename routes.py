from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_mail import Message
from app import mail  # mail 객체를 임포트

# 블루프린트 생성
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('contact.html')

@main_bp.route('/send_message', methods=['POST'])
def send_message():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # 관리자의 이메일로만 메일을 전송합니다.
        msg = Message(f'Contact Form Submission from {name}',
                      recipients=[email])  # 관리자의 이메일로 전송
        msg.body = f"""
        Name: {name}
        Email: {email}
        Message: {message}
        """
        
        try:
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash(f'Failed to send message. Error: {e}', 'danger')

        return redirect(url_for('main.index'))
