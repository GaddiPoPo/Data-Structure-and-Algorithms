class Queue:
    def __init__(self):
        self.__array=[]
        self.__count=0
        self.__front=0
    def enqueue(self,ele):
        self.__array.append(ele)
        self.__count+=1
    def dequeue(self):
        if self.__count==0:
            return -1
        ele=self.__array[self.__front]
        self.__front+=1
        self.__count-=1
        return ele
    def size(self):
        return self.__count
    def isempty (self):
        return self.__count==0
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# while q.isempty() is False:
#     print(q.dequeue())