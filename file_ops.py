import os                                       # use for intrecting with the operating syestem
import platform                          
import subprocess                                        #use to run external program 
from tkinter import messagebox                               #used to show pop error message

def list_files(directory, supported_extensions):
    files = []
    try:
        for f in os.listdir(directory):            #gets all the entries in the floder 
            
            if os.path.isfile(os.path.join(directory, f)):        
                ext = os.path.splitext(f)[1].lower()           #the file extension 
                if ext in supported_extensions:
                    files.append(f)                    #add matchings files to the list
        files.sort()           
    except Exception as e:
        messagebox.showerror("Error", f"Failed to list files: {e}")
    return files

def delete_file(filepath):
    try:
        os.remove(filepath)
        return True                                             #if deletion succeeded
    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete file: {e}")
        return False                                                    #idicates the failure

def open_file(filepath):
    try:
        if platform.system() == 'Windows':
            os.startfile(filepath)
        elif platform.system() == 'Darwin':  # macOS
            subprocess.run(['open', filepath])
        else:
            subprocess.run(['xdg-open', filepath])
        return True 
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open file: {e}")
        return False