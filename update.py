import urllib.request as Url
import tkinter as tk
from tkinter import ttk
import time
#import wget
#import requests
def dwn(url):
    file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = len(u.read())
    print("Downloading: %s Bytes: %s" % (file_name, file_size))

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print(status,end="")

    f.close()
def d(url,filename="cache.txt"):
    with open(filename,"wb") as f:
        vz=Url.urlopen(url).read()
        #vz=str(vz).replace("\\\\",'''\
#''').replace("'","")[1:]
        #vz=vz.replace("\\n",'''\n''')
        print(vz)
        f.write(vz)
        

    return vz
        
def demo():
    


    class SampleApp(tk.Tk):

        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)
            self.title("Update(press start to start)")
            self.button = ttk.Button(text="start update", command=self.start)
            self.button.pack()
            self.progress = ttk.Progressbar(self, orient="horizontal",
                                            length=200, mode="determinate")
            self.progress.pack()

            self.bytes = 0
            self.maxbytes = 50000

        def start(self):
            self.progress["value"] = 0
            self.maxbytes = 50000
            self.progress["maximum"] = 50000
            self.read_bytes()

        def read_bytes(self):
            '''simulate reading 500 bytes; update progress bar'''
            self.bytes += 50
            self.progress["value"] = self.bytes
            if self.bytes==100:
                v=d('https://raw.githubusercontent.com/javaarchive/PIDLE/master/idlelaunch.py', "Updatedidle.py")
            if self.bytes==300:
                v=d('https://raw.githubusercontent.com/javaarchive/PIDLE/master/LAUNCHER.py', "launcher.py")
                time.sleep(10)
            if self.bytes==250:
                v=d('https://raw.githubusercontent.com/javaarchive/extensions/master/cache.txt', "cachesave.txt")
                time.sleep(1)
                
            if self.bytes < self.maxbytes:
                # read more bytes after 100 ms
                self.after(100, self.read_bytes)
            else:
                self.bell()
                self.title("Finished updating")
                self.label=ttk.Label(self,text="Dowbload provoided by Github")
                self.label.pack()

    app = SampleApp()
    app.mainloop()
#urllib.urlretrieve('url_to_file', file_name)
#v=d('https://raw.githubusercontent.com/javaarchive/PIDLE/master/idlelaunch.py', "Updatedidle.py")
demo()    
