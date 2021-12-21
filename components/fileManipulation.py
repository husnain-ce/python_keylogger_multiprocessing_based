
import os,fnmatch

class FileManipulation:
    def __init__(self,order,file_ext=None):
        self.file_li = []
        self.file_find_ext = file_ext
        self.whats_order = order

    def cap_file_list(self):
        for root,subdir,files in os.walk(os.getcwd()):
            for file in files:
                for i in self.file_find_ext:
                    
                    if fnmatch.fnmatch(file,i):
                        all_file_path = os.path.join(root,file)
                    
                        if self.whats_order == "cap_li":
                            self.file_li.append(all_file_path)
                        
                        elif self.whats_order == "rm":
                            os.unlink(all_file_path) 
                        
        return self.file_li                
                        