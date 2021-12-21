import os
import win32clipboard
from multiprocessing import Manager
from ctypes import c_char_p

class CC:
    def __init__(self):
        self.filepath = os.getcwd() + "\\" + "cc.txt"
        self.li = [] 

    # def cpy_clip(self,side_1,side_2):
    def cpy_clip(self,resp):
        while True:
            with open(self.filepath , "a") as f:
                try:
                    win32clipboard.OpenClipboard()
                    pasted_data = win32clipboard.GetClipboardData()
                    
                    flag = False
                    self.li.append(pasted_data)
                    if len(self.li) > 1:
                        if self.li[0] != self.li[1]:
                            print(self.li[0],self.li[1])
                            f.write(pasted_data)
                            self.li = []
                        else:
                            pass

                    elif not flag:
                        f.write(pasted_data)
                        f.write("\n")

                    else:
                        pass

                    win32clipboard.CloseClipboard()
                except:
                    f.write("Clipboard not be copied")
                    
            # check = side_2.recv()
            # if check:
            #     print("I closed after 10 seconds")
            #     break
         
            check =resp.value
            if check:
                print(f"Now the conditions has been true:==> {check}")
                break         
  
  
  
  
  
  
  
  