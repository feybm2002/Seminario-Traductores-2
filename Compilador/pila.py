class Pila:
     def __init__(self):
         self.items = []

     def isempty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def top(self):
         return self.items[len(self.items)-1]

     def lenght(self):
         return len(self.items)
     
     def __str__(self) -> str:
         return self.items.__str__()
