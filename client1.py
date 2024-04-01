import socket
import pickle
HOST=socket.gethostname()
PORT=9999

client1_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1_socket.connect((HOST,PORT))  

# Creating a python object to send
input_type = input("Enter the type of object you want to input (tuple/list/string/integer/dict): ")

if input_type.lower() == 'tuple':
    # Input a tuple
    data = tuple(input("Enter a tuple (comma-separated values): ").split(','))
elif input_type.lower() == 'list':
    # Input a list
    data = list(input("Enter a list (comma-separated values): ").split(','))
elif input_type.lower() == 'string':
    # Input a string
    data = input("Enter a string: ")
elif input_type.lower() == 'integer':
    # Input an integer
    data = int(input("Enter an integer: "))
elif input_type.lower() == 'dict':
    user_input = input("Enter dictionary items (key-value pairs separated by commas): ")

    # Splitting the input string by commas
    items = user_input.split(',')

    # Creating an empty dictionary to store the input items
    data = {}

    # Looping through the items and adding them to the dictionary
    for item in items:
        # Splitting the item by colon to separate key and value
        key_value = item.split(':')
        key = key_value[0].strip()  
        value = key_value[1].strip()  
        data[key] = value
else:
    print("Invalid input type!")


serialized_data = pickle.dumps(data)  

# Send serialized data to server
client1_socket.send(serialized_data)

# Receive response from server
response_data = client1_socket.recv(1024)
if response_data:
    deserialized_response = pickle.loads(response_data) 
    print("Received response from server:", deserialized_response)

# Close client socket
client1_socket.close()
