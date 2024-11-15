## Docker cheat sheet
<p>This command is used to create and start a new Docker container based on a specified image.
</p>
<br>
<b>$ docker run -itd IMAGE_NAME</b>
<br>

<p>
<b>-i or --interactive</b>: flag ensures that the container runs in interactive mode. allowing you to interact with it via the terminal.</p>
<p>
<b>-t or --tty</b>: This flag assigns a pseudo-terminal (TTY) to the container, enabling text-based interaction.</p>
<p>
<b>-d or --detach</b>: This flag runs the container in the background (detached mode), allowing you to continue using the terminal.</p>

#### Building Docker images
With Dockerfile written, you can build the image using the following command:

$ docker build .
<p>We can see the image we just built using the command docker images.</p>

$ docker images

Docker is a tool that helps you package your application and its dependencies into lightweight containers, so it can run consistently across different environments. These containers are like portable, isolated units that work the same way on your computer, a server, or in the cloud.

