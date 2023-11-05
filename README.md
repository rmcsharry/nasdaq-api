# nebula-api
A Fast API server to return nasdaq historical stock quotes.

Note the following files:

**requirements.txt**

&nbsp;&nbsp;&nbsp;&nbsp; This simply lists the dependencies so that on EC2 we can run the following to install them:

&nbsp;&nbsp;&nbsp;&nbsp; `pip3 install -r requirements.txt`


**.fastapi_nginx**

&nbsp;&nbsp;&nbsp;&nbsp; This contains the nginx settings, including the public IP of the EC2 instance (server_name).

&nbsp;&nbsp;&nbsp;&nbsp; This file is deployed to the server in the nginx sites-enabled folder:

&nbsp;&nbsp;&nbsp;&nbsp; `/etc/nginx/sites-enabled/fastapi_nginx`

# Deployment

On commits to `main` a github action will run to deploy to the EC2 instance. The project will deploy to:

`/home/ubuntu/nebula-api`
