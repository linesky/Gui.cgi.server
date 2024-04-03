import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import subprocess
import shutil
import os
import threading
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer
builder =None

def prints(s):
    global builder
    BareboneBuilder.printss(builder,s)


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        command=str(self.path)
        result=""
        try:
            
            scn=command.split("/cgi-bin/")
            lscn=len(scn)
            sscn=command.find(".elf")
            
            if sscn>-1:
                result = subprocess.check_output("."+command, stderr=subprocess.STDOUT, shell=True, text=True)
            elif lscn>1:
                cnd3=scn[1].split("?")
                lcnd3=len(cnd3)
                command="./cgi-bin/"+cnd3[0]
                cnd="./cgi-bin/"+cnd3[0]
                scn4=""
                if lcnd3>1:
                    scn4=cnd3[1]
                    scn4=scn4.replace("_"," ")
                    scn4=scn4.replace("%20"," ")
                prints(cnd)
                f1=open(command)
                command=f1.read()
                f1.close()
                command=command.replace("\r","\n")
                scn1=command.split("\n")
                cnd2=scn1[0]
                cnd2=cnd2.split("#")
                cndl=len(cnd2)
                prints(cnd2)
                if cndl>1:
                    cnd2=cnd2[1]
                    lcnd2=cnd2.find("/")
                    if lcnd2>-1:
                        cnd2=cnd2[lcnd2:]
                    command=cnd2+" "+cnd+" "+scn4


                        
                    prints(command)
                    result = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, text=True)
                else:
                    result="error\n"
            else:
                if command=="/":
                    command="."+command+"index.html"
                else:
                    command="."+command
                f1=open(command)
                result=f1.read()
                f1.close()    
                
            self.send_response(200)
            self.send_header("Content-type",'text/html' )
            self.end_headers()
            bs=(result).encode("utf-8")
            self.wfile.write(bs)
            
        except subprocess.CalledProcessError as e:
            if 0==0:
                
                bs=("Error executing command:\n"+e.output)
                bs=(bs).encode("utf-8")
                self.wfile.write(bs)
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    prints(f'Starting httpd on port {port}...')
    httpd.serve_forever()



class BareboneBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("cgi server")

        # Janela amarela
        self.root.configure(bg='blue')

        # Área de texto
        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack(pady=10)

        # Botões
        self.build_button = tk.Button(self.root, text="clear", command=self.build_kernel)
        self.build_button.pack(pady=5)

        self.run_button = tk.Button(self.root, text="Run", command=self.run_kernel)
        self.run_button.pack(pady=5)
        self.tt=None
        

    def execute_command(self, command,show:bool):
        try:
            
            result = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, text=True)
            self.text_area.insert(tk.END, result)
        except subprocess.CalledProcessError as e:
            if show:
                self.text_area.insert(tk.END,f"Error executing command:\n{e.output}")

    def build_kernel(self):
 
        self.text_area.delete(1.0, tk.END)

    def run_kernel(self):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END,"start server\n")
        self.tt=threading.Thread(target=run)
        self.tt.start()

    def printss(self,s):
         self.text_area.insert(tk.END,s+"\n")



if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
