# Generating_Express_Server
In this project, we are writing a python script that will read json objects in which information about different nodes is present. The python script will automatically generate an Express server and include different middlewares and routes.  

Project Requirements (dependencies) :
  1.  for 'server_script.py' file, python must be installed in the directory.
  2.  for 'server.js' file, node, express and cors must be installed in the directory.


How to run 'server_script.py' file :
  1. open the directory where you have stored 'server_script.py' and 'nodes_info' files.
  2. open command prompt or open this directory in vs code.
       ---Note : python must be installed in this directory.
     
  4. fill the 'json' and 'output' path arguments and run this command ==>
  
          python server_script.py --json path_to_node_config_file --output path_to_directory_where_server.js_will_be_stored

          for example : python script_02.py --json nodes_info.json --output D:/Express_server 


How to install dependencies to run express server.js file:
  1.  for node.js  => download and install node.js from 'https://nodejs.org/en/download'. After this setup environmental variables for node.js
  2.  for express and cors  =>
     
          a).  go to output directory where you want to save your express server js file.
      
          b).  open command prompt or open this directory in vs code 
      
          c).  run this command ==> 'npm install express cors'
      

 
