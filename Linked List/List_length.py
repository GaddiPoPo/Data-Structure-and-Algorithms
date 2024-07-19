def length(self):
    current=self.head
    count=0
    while current!=None:
        count+=1
        current=current.next
    return count