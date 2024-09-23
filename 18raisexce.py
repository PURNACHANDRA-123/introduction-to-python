class accident(Exception):
    def __init__(self,message):
        self.message=message
    def print_exception(self):
        print("user defined exception",self.message)
    def handle(self):
        print("accident occurred. take action")




try:
    raise accident("crash b/w 2 cars")
except accident as e:
    e.handle()











