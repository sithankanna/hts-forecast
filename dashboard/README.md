
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