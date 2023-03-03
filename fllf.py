import socket
import urllib.request, urllib.error, urllib.parse
import re
'''
with open("/tmp/cars.txt","w+") as file:
  car = 0
  for i in range(0,50):
    file.write("There are " + str(i) + " cars\n")
    car+=1
with open("/tmp/cars.txt","r") as file:
    print(file.read())

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('127.0.0.1', 9990))
clientsocket.send('Knock, knock'.encode())
data = clientsocket.recv(1024)
print(data)

response2 = urllib.request.urlopen("http://127.0.0.1:8080/winning")
html = response2.read()
print(html)

html = """
<html>
<head>
    <title>Regex Demo</title>
</head>
<body>
    <div class='firstDiv'>Hello</div>
    <div class='secondDiv'>Hello</div>
</body>
</html>
"""


# CHALLENGE 1: Write a regex search that extracts all the classes from
#             the divs and saves them into an array.
pattern = "class='(.*)'"
data = re.findall(pattern, html)

# CHALLENGE 2: Write a loop that goes through the array from
#              CHALLENGE 1 and prints the contents.

for i in data:
  print(i)

serversocket.listen(10)

# Setup an infinite loop so the socket will keep listening for
# incoming connections.
while True:
  # If it gets a new connection, accept it and save the connection
  # and address.
  connection, address = serversocket.accept()
  # Read 1024 bytes of data from the connection.
  data = connection.recv(1024).decode()
  # Check the length of data. If the length is more than 0 then
  # that means something was sent, so print it out.
  if len(data) > 0:
      print("Received: " + data)

  # Close the connection.
  connection.close()
  # We don't need to keep listening any more so break out of the
  # infinite loop
  break
'''
'''
  We think the six bike reference numbers might be encrypted with a Caesar Cipher
   (which is where the letters are shifted along by a certain offset, e.g. if the letter
    is A and the offset is 2 it will become C), and we've got some intel that one of them
     contains a code that starts with the word "BAR". We've worked out that the offset 
     for each code is determined by the order quantity. See if you can use that to break
      the encryption and find the hidden code.

Tip: The decrypted reference number containing the word BAR is the flag.'''
