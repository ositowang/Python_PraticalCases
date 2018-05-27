from telnetlib import Telnet
from sys import stdin,stdout
from collections import deque

class telnetClient(object):
    def __init__(self,addr, port = 23):
        self.addr = addr
        self.port = port
        self.tn = None


    def start(self):



        # user
        t = self.tn.read_until("login:  ")
        stdout.write(t)
        user = stdin.readline()
        self.tn.write(user)



        # password
        t = self.tn.read_until("Password:  ")
        if t.startswith(user[:-1]):t = t[len(user) + 1:]
        stdout.write(t)
        self.tn.write(stdin.readline())

        t = self.tn.read_until("$  ")
        stdout.write(t)
        while True:
            uniput = stdin.readline()
            if not uniput:
                break
            self.history.append(uniput)
            self.tn.write(uniput)
            t = self.tn.read_until("$  ")
            stdout.write(t[len(uniput) + 1:] )



    def __enter__(self):
        self.tn = Telnet(self.addr, self.port)
        self.history = deque()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.tn.close()
        self.tn = None
        with open(self.addr + "history.txt", "w") as f:
            f.write(self.history)



