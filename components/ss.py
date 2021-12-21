import pyautogui,cv2,time,os,shutil
import numpy as np

class Ss:
    def __init__(self):
        self.curr_dir_path = os.getcwd() + '\\' + "ss"
        self.grabbed_images = []
        self.path_verify()
        
    def path_verify(self):
        if os.path.exists(self.curr_dir_path):
            shutil.rmtree(self.curr_dir_path)
            os.mkdir(self.curr_dir_path)
        else:
            os.mkdir(self.curr_dir_path)
        
    def screen_shot(self,ss_resp):
        while True:
            check = ss_resp.value
            
            for grabed_image in range(0,15):
                grabed_image = pyautogui.screenshot()
                grabed_image = cv2.cvtColor(np.array(grabed_image),
                                cv2.COLOR_RGB2BGR)
                time.sleep(2)
                self.grabbed_images.append(grabed_image)

            for i in range(0,15):
                cv2.imwrite(os.path.join(self.curr_dir_path, "img"+str(i)+".png"), self.grabbed_images[i])

            if check:
                break
        
            
