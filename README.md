# Generating_Express_Server
In this project, we are writing a python script that will read json objects in which information about different nodes is present. The python script will automatically generate an Express server and include different middlewares and routes.  

Project Requirements (dependencies) :
  1.  for 'server_script.py' file, python must be installed in the directory.
  2.  for 'server.js' file, node, express and cors must be installed in the directory.


How to run 'server_script.py' file :
  1. open the directory where you have stored 'server_script.py' and 'nodes_info.json' files.
  2. open command prompt or open this directory in vs-code.

          --- Note : python must be installed in this directory. if not then first download and install python from 'https://www.python.org/downloads/'. After this setup environmental variables for python.
          --- python version : 3.11 or higher 

     
  4. fill the 'json' and 'output' path arguments and run this command ==>
  
          python server_script.py --json path_to_node_config_file --output path_to_directory_where_server.js_will_be_generated

          for example : python server_script.py --json nodes_info.json --output D:/Express_server
       --- Note : if we don't provide an output path, the server.js file will be generated in the current directory of 'script_server.py' file inside a folder "generated server".


How to install dependencies to run express server.js file:
  1.  for node.js  => download and install node.js from 'https://nodejs.org/en/download'. After this setup environmental variables for node.js
  2.  for express and cors  =>
     
          a).  go to output directory where you want to generate your express server 'server.js' file.
      
          b).  open command prompt or open this directory in vs code 
      
          c).  run this command ==> 'npm install express cors'

          d).  version ==>  cors: (2.8.5 or higher), express: (4.21.2 or higher)
      

How to run 'server.js' file that was generated in the output directory by server_script.py file:
   1.  open the output directory in vs-code or command prompt
   2.  run this command ==>  'node server.js'

            --- Note:  node, express and cors must be installed in the output directory

How to Check the functioning of generated server :

  we can use "Postman" => Postman is a API platform for building and using APIs. We can send different types of request to our running server routes and also we can pass different attributes in the request header (like : authorization : admin , authorization : user, etc.) to check the functioning of middlewares.

  --- Note : If we are using Postman then we only enter key = authorization & value = admin, (instead of entering key = 'authorization' & value = 'admin'), because by-default key and value are strings. so we don't need to specify them with in quotes.


