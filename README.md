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


