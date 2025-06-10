#Queue
class Queue():
    def __init__(self):
        self.queue=[]
        self.index=0
        self.numofitems=0
        
    def isempty(self):
        return self.numofitems==0
    
    def enqueue(self,items):
        self.queue.insert(self.index,items)
        self.index+=1
        self.numofitems+=1
        return '{} added to queue'.format(items)
    def dequeue(self):
        if self.isempty()==True:
            return 'Queue is empty'
        else:
            data=self.queue.pop(0)
            self.index+=1
            self.numofitems-=1
            return '{} remove from queue'.format(data)
        
if __name__=='__main__':
    q=Queue()
    
    print(q.enqueue(1))
    print(q.enqueue(2))
    print(q.enqueue(3))
    print(q.enqueue(4))
    print(q.enqueue(5))
    print(q.enqueue(6))
    print(q.enqueue(7))
    
    
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
   