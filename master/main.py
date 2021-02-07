import socket
import time
import threading
import time

# socket init
HOST = "192.168.0.181"
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

_socket = True
command = None


# tello 
SPEED = 20

def makeSocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    while _socket:
        conn, addr = s.accept()
        try:
            if conn:
                global command
                _send = f"command,{command}"
                conn.send(bytes(_send,"utf-8"))
                if command is not None and command.split(",")[0] in ["flip", "takeoff", "land"]:
                    command = None
        except Exception as e:
            print(e)
            conn.close()
threading.Thread(target=makeSocket).start()

while True:
    _cmd = input("Enter commands: ")
    _cmd = _cmd.lower()
    print(_cmd)
    if _cmd == "takeoff":
        command = "takeoff"
        print(command)
    elif _cmd == "land":
        command = "land"
    elif _cmd == "stop":
        command = "stop"
    elif _cmd == "move_forward":
        # left_right_velocity, forward_backward_velocity, up_down_velocity, yaw_velocity
        command = f"move,0,{SPEED},0,0"
    
    elif _cmd == "move_backward":
        # left_right_velocity, forward_backward_velocity, up_down_velocity, yaw_velocity
        command = f"move,0,{-SPEED},0,0"
    
    elif _cmd == "move_up":
        # left_right_velocity, forward_backward_velocity, up_down_velocity, yaw_velocity
        command = f"move,0,0,{SPEED},0"
    
    elif _cmd == "move_down":
        # left_right_velocity, forward_backward_velocity, up_down_velocity, yaw_velocity
        command = f"move,0,0,{-SPEED},0"

    elif _cmd == "move_left":
        # left_right_velocity, forward_backward_velocity, up_down_velocity, yaw_velocity
        command = f"move,{SPEED},0,0,0"
    
    elif _cmd == "move_right":
        # left_right_velocity, forward_backward_velocity, up_down_velocity, yaw_velocity
        command = f"move,{-SPEED},0,0,0"

    elif _cmd == "rotate_left":
        # left_right_velocity, forward_backward_velocity, up_down_velocity, yaw_velocity
        command = f"move,0,0,0,{SPEED}"
    elif _cmd == "rotate_right":
        # left_right_velocity, forward_backward_velocity, up_down_velocity, yaw_velocity
        command = f"move,0,0,0,{-SPEED}"
    
    elif _cmd == "flip_right":
        command = f"flip,r"
        
    elif _cmd == "flip_left":
        command = f"flip,l"
        
    elif _cmd == "flip_forward":
        command = f"flip,f"
        
    elif _cmd == "flip_backward":
        command = f"flip,b"
    
    elif _cmd == "land":
        command = "land"
    elif _cmd == "exit":
        command = None
        _socket = False
        command = "quit"
        break
    else:
        print("Command not found")
    time.sleep(0.4)
