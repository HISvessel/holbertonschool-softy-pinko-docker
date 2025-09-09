Henlo. And welcome to shipping applications with Docker.


What is Docker? It is a platform that allows you to create containers for your apps, so that they can be packaged and shipped into any environment as self contained environments. 

To understand the concept of shipping with docker, for this project, an infrastructure will be created that uses a reverse proxy,a load balancer, two application servers and a single front-end server.

First off: what is Docker?
-> it is an open platform for developing, shipping and running applications. It is a tool utilized for separating the app from its infrastructure for software delivery. 

-> the Docker platform provides the ability to package and run an application in a loosely isolated environment, a secure place for running multiple containers on a given host in a lightweight, concise and safe way. These containers can be shared while they are being worked upon. 

WHat is Docker used for?
-> streamlining the development lifecycle by allowing developers to work in standardized environments using local containers which provide the app and its services. These containers are great for Continuous Integration and Continuous Delivery(CI/CD) workflows.
-> These containers provide a very flexible workflow that can see developers work in the working environment and push changes to the container that is shared into the testing environment for manual and automated tests, which is then sent to the consumer's emnvironment if testing is successful or to the work environment if further testing is necessary. 

Docker Architecture
-> docker uses a client-server architecture: the client talks to the Docker daemon, which builds runs and distributes the containers. The client-daemon relationship can run on the same system, or the connection can be a established remotely. Communication between both entities is established by the use of REST APIs, over UNIX sockets or a network interface. 
    >> The docker daemon(dockerd) listens for DOcker API requests and manages Docker objects such as images, containers, networks and volumes. A daemon can also communicate with other daemons to manage Docker services. 
    >> the docker client is the primary way that many Docker users interact with Docker. Using commands like docker run can allow the client to send coomands to the docker daemon to carry out the request. The client can communicate with more than a single daemon, meaning multiple requests can be made. 
    >> the docker desktop is an environment that permits the building and sharing of containerized applications and microservices, that is easy to install on the MacOS, Windows or Linux environment. These desktops include the daemon, client, Docker compose, Docker Content Trust, Kubernetes, and Credential Helper. 
    >> Docker registries can store docker images. 
    >>Docker objects are items that are tied to the funcionality of containers for shipping, such as using images, containers, networks, volumes, plugins, etc. 
      1) Images- This is a read only template with instructions for creating a Docker container. Images are compounded to other images with additional set of instructions and customizations. You can create images to use and distribute into a registry, or you can simply use other images. To builld your own Docker image, you create a Dockerfile with a simple syntax for defining the steos needed to create the image and run it. Layers are created inside of an image with the isertion of instructions. Rebuilding images changes the rebuilt layers, the rest remain the same. 
      2) containers - a container is a runnable instance of an image which you can create, start, stop, move or delete using the Docker API or the CLI. A container can be connected to one or more networks, attach storage to it or even create a new image based on its current state. 

      