import json
import os
import argparse


# Read json file

def read_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)



# Parsing json data
# We can normally iterate over the JSON data, but using a dictionary with id as the key makes it easy and fast to look up nodes.
# When directly iterating over json data, if we require to find a node with a specific id, then we have to loop through all nodes every time. This makes lookups slower for large datasets.
def parse_nodes(data):
    nodes = {node["id"]: node for node in data["nodes"]}
    return nodes







# Server Creation Logic


def generate_express_server(nodes, output_dir):
    # Start building the Express server code

    # Set up required imports based on node properties
    required_imports = {
        "express": True,  # Express is always required
        "cors": any(node["properties"].get("type") == "middleware" and "allowed_origins" in node["properties"] for node in nodes.values())
    }



    server_code = "\n".join([
        'const express = require("express");',
        'const cors = require("cors");' if required_imports["cors"] else "",
        "",
        "const app = express();",
        "app.use(express.json());",
        "app.use(cors());" if required_imports["cors"] else "",
        "\n"
    ])

    # ==>   We Will handle Middlewaare first :
    
    # Adding middleware based on node properties
    
    # above for loop is returning a tuple 'node' so we cannot iterate it simply like ' node["properties"]["type"] '
    # that's why we used 'node_id' also, this will unpack the 'node' tuple
    for node_id, node in nodes.items():
        
        # Also we cannot use ==> node["properties"]["type"],  because 'type' is not present in properties dictionary of all the json objects.
        # Hence it will through error if 'type' is not found. that's why we have used get() method.
        
        if node["properties"].get("type") == "middleware":
            
            # checking if the current object is representing "CORS middleware" 
            if "allowed_origins" in node["properties"]:
                # Handle CORS Middleware
                
                allowed_origins = node["properties"]["allowed_origins"]
                server_code += f"""
// CORS Middleware - {node['name']}
app.use(cors({{ origin: {allowed_origins} }}));
"""


            # checking if the current object is representing "Auth middleware" 
            if "auth_required" in node["properties"] and node["properties"]["auth_required"] == True:
                # Handle Auth Middleware
                
                server_code += f"""
// Auth Middleware - {node['name']}
const authMiddleware = (req, res, next) => {{
    if (!req.headers.authorization) {{
        return res.status(401).json({{ message: "Unauthorized" }});
    }}
    next();
}};
"""


            # checking if the current object is representing "Admin auth middleware" 
            if "admin_required" in node["properties"] and node["properties"]["admin_required"]:
                # Handle Admin Auth Middleware
                
                server_code += f"""
// Admin Auth Middleware - {node['name']}
const adminMiddleware = (req, res, next) => {{
    if (!req.headers.authorization || req.headers.authorization !== 'admin') {{
        return res.status(403).json({{ message: "Forbidden" }});
    }}
    next();
}};
"""
                

            # checking if the current object is representing "Login Middleware"
            # It logs the request method (GET, POST, etc.) and the endpoint (/login, /signup).
            # Then it calls next(); to continue processing the request.
            # it write in console : "LOG: POST request to /login", so by checking logs, it is easy to debug and find errors
            if "log_requests" in node["properties"] and node["properties"]["log_requests"]:
                # Handle Logging Middleware
                
                server_code += f"""
// Logging Middleware - {node['name']}
app.use((req, res, next) => {{
    console.log(`${{req.method}} ${{req.url}}`);
    next();
}});
"""





    #   ==>     Now we will handle routes : 
    
    # Finding and adding routes based on node properties andd endpoints
    for node_id, node in nodes.items():
        
        if "endpoint" in node["properties"]:
            endpoint = node["properties"]["endpoint"]
            method = node["properties"]["method"].lower()


            # Handle the GET routes that don't require middleware interfarence
            if method == "get" and endpoint not in ["/user", "/admin"]:
                
                server_code += f"""
// {node['name']} - GET {endpoint}
"""

                if endpoint == "/home" :
                    server_code += f"""
app.get("/home", (req, res) => {{
    res.json({{ message: "Welcome to Home Page" }});
}});
"""
                elif endpoint == "/about" :
                    server_code += f"""
app.get("/about", (req, res) => {{
    res.json({{ message: "About us" }});
}});
"""
                elif endpoint == "/news" :
                    server_code += f"""
app.get("/news", (req, res) => {{
    res.json({{ message: "Latest news" }});
}});
"""

                elif endpoint == "/blogs" :
                    server_code += f"""
app.get("/blogs", (req, res) => {{
    res.json({{ message: "Blogs list" }});
}});
"""


            # Handle the GET routes that require middleware interfarence
            elif method == "get" and endpoint in ["/user", "/admin"]:
                
                server_code += f"""
// {node['name']} - GET {endpoint}
"""
                # for "/user"
                if endpoint == "/user" :
                    server_code += f"""
app.get("/user", authMiddleware, (req, res) => {{
    res.json({{ message: "User data" }});
}});        
"""
                # for "/admin"
                elif endpoint == "/admin" :
                    server_code += f"""
app.get("/admin", authMiddleware, adminMiddleware, (req, res) => {{
    res.json({{ message: "Admin data" }});
}});        
"""


            # Handle the POST routes 
            elif method == "post":
                
                server_code += f"""
// {node['name']} - POST {endpoint}
"""
                
                if endpoint == "/login" :
                    server_code += f"""
app.post("/login", (req, res) => {{
    res.json({{ message: "Login successful" }});
}});
"""
                elif endpoint == "/signup" :
                    server_code += f"""
app.post("/signup", (req, res) => {{
    res.json({{ message: "Signup successful" }});
}});
"""

                elif endpoint == "/signout" :
                    server_code += f"""
app.post("/signout", (req, res) => {{
    res.json({{ message: "Signout successful" }});
}});                
"""




    # TO handle invalid routes :
    server_code += """
// Handle invalid routes    
app.use((req, res) => {
    res.status(404).json({ error: "Route not found" });
});
"""




    # End the server setup

    #specify the port
    port = 3000

    server_code += f"""
// run server on {port} port     
app.listen({port}, () => console.log("Server running on http://localhost:{port}"));
"""

    # Write to the output directory
    with open(os.path.join(output_dir, "server.js"), "w") as file:
        file.write(server_code)








# Main Function

def main():
    # argparse is a Python module that allows us to handle command-line arguments.
    parser = argparse.ArgumentParser()

    # We Are adding 2 arguments 'json' and 'output' in user input.
    parser.add_argument("--json", required=True, help="Path to JSON configuration file")
    parser.add_argument("--output", default="generated_server", help="Output directory")

    # noW, processes the user input:  
        #  ==> parser.parse_args() function returns an object called Namespace
        #  ==> 'Namespace' is a simple object that acts like a container for storing values. It stores each argument as an attribute (like a variable inside an object)
    args = parser.parse_args()

    # now, we can access the arguments like : args.json and args.output

    # reading the json file
    data = read_json(args.json)

    # creating a dictionary for fast lookup --> although it is optional, we can directly work with json data
    nodes = parse_nodes(data)

    # creating a directory (if not present already)
    os.makedirs(args.output, exist_ok=True)

    # function for generating express server
    generate_express_server(nodes, args.output)
    
    print(f"Express server generated in {args.output}/")


if __name__ == "__main__":
    main()
