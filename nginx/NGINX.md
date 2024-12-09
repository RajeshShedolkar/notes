Nginx is a high-performance web server and reverse proxy server used for serving web content, load balancing, and handling large amounts of traffic efficiently.
It is widely used for serving static content, load balancing, and handling HTTP requests efficiently. Its lightweight architecture makes it ideal for modern web applications and microservices.
spin off ubuntu container<br>
```$ docker run -it -p 8080:80 ubuntu```

in ubuntu terminal:<br>
```audo apt-get install```<br>
```sudo apt-get install nginx```

The following is the file structure after installation.
<img src="image.png" width="900" height="300">

After executing following command 
```$ nginx``` 

On localhost, Nginx displays the default page, which typically executes on port 80. However, since I have mapped port 8080 to port 80, it now appears on port 8080.<br>
<img src="image-2.png" width="800" height="400">

Basic nginx.conf<br>
<img src="image-3.png" width="600" height="500">

Reload Nginx server by using following command<br>
```nginx -s reload```

-s reload sends a signal to instruct nginx to reload its configuration file without actually stopping and starting the process.
![alt text](image-4.png)



Serve static content:
I added an HTML index file to the mysite directory. Now the Nginx configuration looks like this:

```
events {

}

http {
    server {
        listen 80;
        server_name _;
        root /etc/nginx/mysite/;
    }
}
```

<img src="image-6.png" width="500" height="100">

<p>Home Page</p>

<img src="image-5.png" width="500" height="300">

<p>
<b>forward request to proxy server:<br></b>
 proxy_pass "http://X.X.X.X:PORT$request_uri";

</p>
NGINX WEBSEVER
