class TrafficLights:
    def __init__(self, street):
        self.green = False
        self.queue = []
        self.street = street
    
    def length(self):
        return len(self.queue)

    def add(self, car):
        self.queue.append(car)

    def remove(self, car):
        return self.queue.pop()

    def __gt__(self, other):
        if self.length() >= other.length():
            return True
        else:
            return False
    
    def __lt__(self, other):
        if self.length() <= other.length():
            return True
        else:
            return False

one = TrafficLights("George")
two = TrafficLights("George")

one.add(12)
one.add(12)
two.add(12)
two.add(12)
two.add(12)
print(max(one,two).length())