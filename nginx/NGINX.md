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

-s reload sends a signal to instruct nginx to reload its configuration file without actually stopping and starting the process.<br>
![alt text](image-4.png)


<br>
Serve static content:<br>
I added an HTML index file to the mysite directory. Now the Nginx configuration looks like this:
<br>
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
![alt text](image-6.png)
<br>
Home Page
![alt text](image-5.png)


 



