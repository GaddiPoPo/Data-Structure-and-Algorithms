class stack:
    def __init__(self):
        self.__array = []

    def push(self, ele):
        self.__array.append(ele)

    def pop(self):
        if self.Isempty():
            print("empty stack")
            return
        return self.__array.pop()

    def top(self):
        if self.Isempty():
            print("no element")
            return
        return self.__array[-1]

    def size(self):
        return (len(self.__array))

    def Isempty(self):
        return
        self.size() == 0
