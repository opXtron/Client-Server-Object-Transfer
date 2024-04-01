import socket
import pickle
HOST=socket.gethostname()
PORT=9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST,PORT))  
server_socket.listen(5)  

print(f'Server is listening for incoming connections on the port:{PORT}\n')
a=[] 
top=-1 

while True: 

    client_socket, client_address = server_socket.accept()
    print(f"Client connected: {client_address}")
    
    received_data = client_socket.recv(1024)
    deserialized_data = pickle.loads(received_data)
    print("Received data from client:", deserialized_data)
    print(f"Type of object: {type(deserialized_data).__name__}")
    
    if(type(deserialized_data).__name__=="dict" and deserialized_data.get("request")=='get_data'):    
        if(top!=-1):
            response_data=a[0]
            serialized_response = pickle.dumps(response_data) 
            client_socket.send(serialized_response)
            a.pop(0)
            top=top-1
        else:
            response_data={'message': 'No objects received from the client'}
            serialized_response = pickle.dumps(response_data) 
            client_socket.send(serialized_response)
    
    else:  #client1
        if(type(deserialized_data).__name__=="dict"):
            a.append(deserialized_data.copy())
        else:
            a.append(deserialized_data)
        top=top+1
    
        response_data = {'message': 'Data received successfully'}
        serialized_response = pickle.dumps(response_data) 
        client_socket.send(serialized_response)
        
    print(f'Objects in the buffer/queue={top+1}')
    print()

    # Close client socket
    client_socket.close()
   
'''
while True:
        msg=s.recv(16) #1024 buffer size
        if new_msg:
            print()
            print(f'The header size: {HEADER_SIZE}')
            msglen= int(msg[:HEADER_SIZE])
            print()
            print(f"new message length: {msglen}")
            new_msg=False
            
        #full_msg+=msg.decode("utf-8")
        full_msg+=msg
        if(len(full_msg)-HEADER_SIZE==msglen):
            print("Full msg has been received")
            print()
            print(f'The header info:\n{full_msg[HEADER_SIZE:]}')
            print()
            d=pickle.loads(full_msg[HEADER_SIZE:])
            print(f'The received object:\n{d}')
            print()
            print(f'Type of the object: {type(d)}')
            
            new_msg=True
            full_msg=b''
        #print(msg.decode("utf-8")) #decode the bytes
    print(full_msg)
'''
