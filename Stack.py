#Stack
class Stack():
    def __init__(self):
        self.stack=[]
        self.numofitems=0
        
    def isempty(self):
        return self.numofitems==0
    
    def push(self,item):
        self.stack.insert(self.numofitems,item)
        self.numofitems+=1
        return '{} pushed to stack'.format(item)
    
    def pop(self):
        if self.isempty()==True:
            return 'Stack is empty'
        else:
            self.numofitems-=1
            data=self.stack.pop(self.numofitems)
            
            return '{} pop from stack'.format(data)
        
    def stacksize(self):
        return len(self.stack)
    
        
        
s=Stack()
print(s.push(1))
print(s.push(2))
print(s.push(3)) 

print("\n\n")
 
print(s.pop())




