Jacob Miesner
Project 01
CS 3610

This project was hosted, developed, and debugged using Fedora Linux VM on my windows 
laptop. I have uploaded the deliverables (web_server.py, client_browser.py, and the 
two png output files) into the main repository.

Web server:
For the web server, I opened up the terminal and ran the web server such that 
it was listening for any requests. I then opened firefox, typed in the local port and ip 
followed by the file I requested in the search bar of firefox. The web server processed 
these requests and sent the data back to the browser I was using and displayed the data.
When a purposely incorrect filename was input, the web server correctly sent back the 404 
not found file.

Web client:
For the web client, I ran the local server I previously made, and ran the default (no
 system args) program and the web client output the raw html data back to the command 
line. Then, I tried to use info.cern.ch as a server and my client I made. I input the 
hostname (info.cern.ch), the port (80) and the file I wished to request (/) which was 
just the home-index page. The data was correctly sent back to the client and displayed 
on the command line.


