sudo rm -rf /etc/nginx/sites-enabled/default

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/nginx_2_1_11.conf

sudo /etc/init.d/nginx restart

sudo gunicorn -w 2 -c /home/box/web/etc/qa.py ask.wsgi:application
