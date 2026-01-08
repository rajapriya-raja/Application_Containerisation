                                                              PROJECT 1
                                                    Application Containerization  

Following steps to Create a Docker image for a static website and run it successfully on a specific port.  

Create a folder (application) 

    sudo mkdir -p /var/www/application

Inside that create a index.html file. 

     sudo nano /var/www/application/index.html

  Inside 
  
     Hii Rajapriya Welcome to Icodex Family

 Save the added content. 
 
Create a nginx server file with the below required commands

    sudo nano /etc/nginx/sites-available/application  -- To create a server configuration 
  
  Inside configuration file
  
       server {

       listen 8028;
       
       server_name 192.168.1.10;
       
       root /var/www/application;
       
       index index.html;
       
       location / {

       try_files $uri $uri/ =404;
       
       }

       }
       
  sudo ln -s /etc/nginx/sites-available/application /etc/nginx/sites-enabled/   --  enable the needed sites 
  
   sudo nginx -t    --  check the status
  
  Check in browser with Ip address in browser   (http://192.168.1.10:8028)

  <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/74c939e8-f2f9-4f2d-97b2-d446bab218a6" />

Create Dockerfile 

Inside   

       FROM nginx:latest 
       
       COPY . /usr/share/nginx/html 
       
       EXPOSE 80 

Build an image with this command 

      Docker build –t contain . 

Run docker container in background 

     Docker run –d –p 8028:80 –name contersation contain 

 9.Run in browser 
 
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f1f07162-3c1d-461e-92af-87b606cfae62" />

10.Verify container is running  
       
                 docker ps 

Push image to the dockerhub with the following commands 

    docker login -u username 

    docker tag tagname username/imagename 

    docker push username/imagename 
 
Check in dockerhub image is pushed 

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/38b29933-eab0-40d3-bbbf-7c4ee169fe17" />

Push container into a Github 

     Download the files from mobaxterm to a windows
   
     Create a Github Repository
   
     Clone the url 
   
       git clone https://github.com/rajapriya-raja/Application_Containerisation
     
       git status
     
       git add .
     
       git status
     
       git commit -m "Commit messages"
     
       git push




                                                                      PROJECT 2: 
                                                                   Data Persistence 

Demonstrate how to manage stateful data in a containerized environment to 
prevent data loss during container lifecycles. 

Create a folder 

      sudo mkdir –p /var/www/persistence 
      
Change a directory inside that ,    
 
Create a python file with the following command, 
  
     sudo nano app.py 
 
Inside that ,  
 
     import time 
     from datetime import datetime 

     FILE_PATH  =“/detail/log.txt” 

     while True: 
         with open(FILE_PATH, "a") as file: 
              file.write(f"Welcome Devops{datetime.now()}\n") 
         print("Python Inprogress") 
         time.sleep(5) 
 
 
Create a Dockerfile to write a configurations, 
 
       sudo nano Dockerfile 
 
Inside that  add a configurations here,     

           FROM   python:3.11-slim 
        
           WORKDIR /app 
 
           COPY app.py  . 
 
           ENTRYPOINT["python", "app.py"]   
 
Build an image 

        sudo docker build –t pyimage  . 

Check images is created with this command  

          sudo docker images 

Create a volume with the following  commands 
 
           sudo  docker volume create  pyvolume 
 
Check volume is created  
 
           sudo docker volume ls 
 
it  listed  the created volumes 
 
 <img width="918" height="155" alt="image" src="https://github.com/user-attachments/assets/1c482ef5-537d-4ded-a528-abe6fa3214b7" />

Run a container  
 
           sudo docker run –d  --name pycontainer  -v   pyvolume:/detail pyimage 
 
Execute a  volume  

  sudo docker exec –it pycontainer  cat /detail/log.txt 
 
it show the  output of the log files 
 
Now we have to check persistence is working, 
 
First stop  the container   

      sudo docker stop pycontainer 
 
Remove the container 

       sudo docker rm pycontainer 

Check the log files it is showing the content with this command 
      
       sudo docker exec –it pycontainer  cat /detail/log.tx 
 
Create a another container then check check the log files there   
 
Also have to create it in a same volume with a different container name  
 
       sudo docker run –d  --name pycontainer1 -v   pyvolume:/detail pyimage 

       To check logs with this command 

      sudo docker log pycontainer1

It show like this

<img width="946" height="448" alt="image" src="https://github.com/user-attachments/assets/8f613756-18f7-46ce-b6f0-7be07f3e1cf1" />
 
Check the log files it is showing the content with this command 
 
        sudo docker exec –it pycontainer1  cat /detail/log.tx 
        
It show old and new datas here,  
 <img width="905" height="174" alt="image" src="https://github.com/user-attachments/assets/2e49f041-a0db-4d57-b11b-095d8bb89025" />
 
Then push a image into a docker hub 
 
             sudo docker login  -u username 
             
             sudo docker tag pyimage username/ pyimage 
            
             sudo docker push username/ pyimage 

 
<img width="1876" height="447" alt="image" src="https://github.com/user-attachments/assets/f9a9e926-2383-4555-a24e-28631db00538" />

Push container into a Github  

Download the files from mobaxterm to a windows 
 
In terminal  do those commands ,  
 
     git status 

     git add . 

     git status 

     git commit -m "Commit messages" 

     git pull origin main 
     
     git push origin main 

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/789dbe12-bcb5-4f55-8461-8d1b6b3f8be6" />


                                                                   PROJECT 3
                                                            Multi-Container Networking 

Architect a system where two distinct containers communicate with each other over a private network using service discovery (DNS), rather than IP addresses. 

Create a folder  
 
    sudo mkdir –p /var/www/networking 

Go inside a folder 
 
    cd /var/www/networking 

Create a docker-compose file  inside write all containers in a single yml file 

     sudo  nano docker-compose.yml 

Inside 

    version: "3.9" 
      
    services: 
       priya: 
          image: redis:7 
          container_name: redisserver  
          networks: 
              - redis-net 

       client: 
          image: redis:7 
          container_name: redisclient 
          depends_on: 
            - priya 
          networks: 
           - redis-net 
          command: ["sleep", "infinity"] 
        
        networks: 
          redis-net:      (redis-net is a user-defined custom bridge network, not the default bridge.) 
            driver: bridge 
    
Run the docker-compose with this command  
       sudo docker-compose up –d  

Check container is running  
       
     sudo docker ps 

Access a client container 
     sudo  docker exec –it redisclient bash 

Connect to redis service using service name  
      redis-cli –h priya 
 
then give input to test 
       PING 

  Output
       PONG 

<img width="1276" height="250" alt="image" src="https://github.com/user-attachments/assets/95189216-22cd-48db-8543-caaa037eaa7e" />
