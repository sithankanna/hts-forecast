
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