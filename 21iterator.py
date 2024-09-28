class remotecontrol:
    def __init__(self):
        self.channel = ["HBO", "CNN", "9X", "Discovery", "HBO2"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channel):
            
            raise StopIteration
        
        return self.channel[self.index]


r = remotecontrol()
iterator = iter(r)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

