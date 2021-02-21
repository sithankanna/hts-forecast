
```bash
streamlit run app.py
```

ssh -i "streamlit_hello_world.pem" ubuntu@ec2-18-219-25-93.us-east-2.compute.amazonaws.com
sudo ln -s /etc/nginx/sites-available/fakeai.org /etc/nginx/sites-enabled/
nano /var/www/fakeai.org/html/index.html
sudo nano /etc/nginx/sites-available/fakeai.org

server {
        listen 80;
        listen [::]:80;

        root /var/www/fakeai.org/html;
        index index.html index.htm index.nginx-debian.html;

        server_name fakeai.org www.fakeai.org;

        location / {
                try_files $uri $uri/ =404;
        }
}
streamlit run dashboard/app.py --server.enableCORS=false

rewrite /my_prefix/(.*) /$1  break;

server {
    listen 80 default_server;
    root /home/ubuntu/public_html;

    location /application1 {  }

    location /images {
        root /home/ubuntu/data;
    }

    location /stream {
        rewrite /stream/(.*) /$1 break;
        proxy_pass http://127.0.0.1:8501/;
        proxy_http_version 1.1;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_read_timeout 86400;
    }

    location / {
        proxy_pass http://127.0.0.1:8501;
        proxy_http_version 1.1;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_read_timeout 86400;
   }


}


sudo nano /etc/nginx/conf.d/server1.conf
sudo nginx -s reload

server {
    listen 80 default_server;
    root /home/ubuntu/public_html;

    location /application1 {  }

    location /images {
        root /home/ubuntu/data;
    }

    location /stream/ {
        rewrite ^/stream/(.*)$ /$1 break;
        proxy_pass http://127.0.0.1:8501/;
        proxy_http_version 1.1;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_read_timeout 86400;
    }

}


Setting up nginx

https://www.nginx.com/blog/setting-up-nginx/#open-web-page



<!-- ## To Do: Dockerize -->



curl https://pyenv.run | bash


Add the following lines to your ~/.bashrc:

export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"


source ~/.bashrc
Install the Python build dependencies for your platform, using one of the commands listed in the official instructions. For example, on a recent Ubuntu this would be:

sudo apt update && sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
You’re ready to install the latest Python releases. This may take a while:

pyenv install 3.8.2


pyenv local 3.8.2


<!-- Install Poetry  -->
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

source ~/.poetry/env




