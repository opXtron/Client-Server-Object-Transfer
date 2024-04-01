import socket
import pickle
HOST=socket.gethostname()
PORT=9999

# Creating a socket
client2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client2_socket.connect((HOST,PORT))  


# request to server to get the object
request_data = {'request': 'get_data'}
serialized_request = pickle.dumps(request_data)  
client2_socket.send(serialized_request)


# receiving the object from the server
response_data = client2_socket.recv(1024)
if response_data:
    deserialized_response = pickle.loads(response_data)  
    print("Received response from server:", deserialized_response)
    print(f"Type of object: {type(deserialized_response).__name__}")

# Closing the socket
client2_socket.close()
