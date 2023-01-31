class one:
    def __init__(self, name):
        self.name = name
        self.time = 0

    def work(self, time):
        self.time = time-1


class two(one):
    def __init__(self, name, time):
        self.time = time+1
        self.work(time)
        super().__init__(name)


d = two("Mike", 2)
print(d.time)
