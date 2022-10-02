sudo chown -R $USER:$USER /var/www/34.143.158.179/html
sudo chmod -R 755 /var/www/34.143.158.179
sudo nano /etc/nginx/sites-available/34.143.158.179
sudo ln -s /etc/nginx/sites-available/34.143.158.179 /etc/nginx/sites-enabled/
34.143.158.179
http://34.143.158.179/