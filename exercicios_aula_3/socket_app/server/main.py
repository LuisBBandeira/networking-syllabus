import socket

HOST = "0.0.0.0"
PORT = 545  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) 
    s.listen()  
    print(f"Server listening on {HOST}:{PORT}")
    
    conn, addr = s.accept()  
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)  
            if not data:  
                break
            conn.sendall(data) 
