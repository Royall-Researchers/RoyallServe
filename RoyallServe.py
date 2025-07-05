import http.server
import socketserver
import os
import subprocess

# Set the port number you want to use
port = 8080
print ("""
RoyallServe is made by
    ____                   _ _ 
   |  _ \ ___  _   _  __ _| | |
   | |_) / _ \| | | |/ _` | | |
   |  _ < (_) | |_| | (_| | | |  
   |_| \_\___/ \__, |\__,_|_|_|
               |___/           
    ____                               _                   
   |  _ \ ___  ___  ___  __ _ _ __ ___| |__   ___ _ __ ___  
   | |_) / _ \/ __|/ _ \/ _` | '__/ __| '_ \ / _ \ '__/ __|
   |  _ <  __/\__ \  __/ (_| | | | (__| | | |  __/ |  \__ \ 
   |_| \_\___||___/\___|\__,_|_|  \___|_| |_|\___|_|  |___/
 

Web-Server has been Started
default port is 8080
default directory is /var/www/html/
open url default = http://localhost:8080/ or http://127.0.0.1/8080
                 
""")

# Change to the directory where your website files are located
web_directory = "/var/www/html/"

# Create a simple HTTP server
handler = http.server.SimpleHTTPRequestHandler

# Change to the specified directory
os.chdir(web_directory)
php_command = f"php -S 0.0.0.0:{port}"
subprocess.run(php_command, shell=True)
# Start the server
with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Serving on port {port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer shutting down.")

