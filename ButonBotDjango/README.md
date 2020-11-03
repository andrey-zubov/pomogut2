# HelpBot
- Chat-bot will tell you where to contact (call/find organisation) in a situation of domestic violence.
- Technologies: Django, Django-MPTT, jQuery, Ajax, HTML, CSS, Telegram Bot API, Yandex JS API.

# Deploy:
- <code>docker-compose build</code>
- <code>docker-compose up -d</code>
- <code>docker exec -it django_web bash</code>
- root@...:/src#<code>python3 manage.py collectstatic</code>
- root@...:/src#<code>python3 manage.py loaddata initial_data.json</code>

# Test Telegram ping
- see 'new 1.txt'
- change bot token
- change chat id (@userinfobot)
- enter command to console
- see result (form in the 'curl-format.txt')


/admin
name: superadmin
pass: TDjymYHSJkpzp4p

# pythonanywhere Tasks
### Scheduled tasks: 
/home/YOURNAME/.virtualenvs/bot_venv/bin/python /home/YOURNAME/ButonBotDjango/ButonBotDjango/help_bot/telega.py