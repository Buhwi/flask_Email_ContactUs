# email활용하여 문의하기 기능 구현
> flask 활용하여 문의하기(contact) 기능 구현

> 문의하기 버튼 클릭시 지정한 email(관리자 계정)으로 문의사항이 전송되게 구현

## 개발환경
```bash
python
html
```

## 환경설정
```bash
$ pip install -r requirements.txt
```

## .env 설정
```bash
$ mkdir .env

# .env
MAIL_USERNAME='관리자 email@google.com'
MAIL_PASSWORD='email password(일반 비밀번호 X)'
```

### google email 연동시 주의사항
> 비밀번호 입력시 앱 비밀번호로 입력 해야함
