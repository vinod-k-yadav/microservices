# Microservices
Basic implementation of microservices using Python , Flask and Docker.
The purpose of this repo is only demonstrate the concept of  microservices using python and how to microservices communicate each others.

Used Flask as web framework to demonstrate the microservices. Used REDIS key-value database server.

Microservices:
   
    UserServices :-  Handles all user realted activity like login/logout and authoriazation etc.
    ProductServcies: Handles product related requests like getting all products deatils or query specific product.
    OrderServices: handles Order related stuff like placing and creating order.
    FrontendServices : This handles all frontend related stuff or interacting with end user.
    
  ![This is an image](./image1.png)

# Intergrating Kubernetes and Docker.

Created multiple pods each for fornetend , backend and data. and deploy microservices using Kubernetes

Architecture diagram:

![mutlipod-architecture1](https://github.com/vinod-k-yadav/microservices/assets/6715521/7f8f3f02-5dc8-4f8a-aa75-df9c0a80fc3b)





 

    
