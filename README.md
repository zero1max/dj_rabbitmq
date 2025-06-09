# Django RabbitMQ Feedback Form

Bu loyiha Django, Celery, RabbitMQ va Redis yordamida asinxron email yuborish imkoniyatini ko'rsatadi.

## Talablar

- Python 3.8+
- Django 5.2+
- Celery
- RabbitMQ
- Redis
- python-dotenv

## O'rnatish

1. Virtual muhitni yarating va faollashtiring:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Kerakli paketlarni o'rnating:
```bash
pip install django celery redis python-dotenv
```

3. RabbitMQ ni o'rnating:
```bash
docker run -d --hostname my-rabbit --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

4. RabbitMQ foydalanuvchisini yarating:
```bash
rabbitmqctl add_user myuser 1
rabbitmqctl set_user_tags myuser administrator
rabbitmqctl set_permissions -p / myuser ".*" ".*" ".*"
```

5. Redis ni o'rnating va ishga tushiring

6. `.env` faylini yarating:
```
DJ_SECRET_KEY=your_secret_key_here
EMAIL_HOST_PASSWORD=your_gmail_app_password_here
```

## Ishlatish

1. Ma'lumotlar bazasini yarating:
```bash
python manage.py migrate
```

2. Celery worker ni ishga tushiring:
```bash
celery -A core worker -l info
```

3. Django server ni ishga tushiring:
```bash
python manage.py runserver
```

4. Brauzerda http://localhost:8000 manzilini oching

## Xususiyatlar

- Foydalanuvchilar feedback formani to'ldirib, email orqali xabar yuborishlari mumkin
- Email yuborish asinxron tarzda Celery orqali amalga oshiriladi
- RabbitMQ message broker sifatida ishlatiladi
- Redis result backend sifatida ishlatiladi

## Muhim eslatmalar

- Gmail uchun App Password yaratishingiz kerak
- Production muhitida DEBUG = False qilib, ALLOWED_HOSTS ni to'g'ri sozlashingiz kerak
- Xavfsizlik uchun .env faylidagi maxfiy kalitlarni himoya qiling