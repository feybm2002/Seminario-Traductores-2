class Pila:
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isempty():
            return self.items.pop()
        else:
            return None  # Otra opción es lanzar una excepción indicando que la pila está vacía

    def top(self):
        if not self.isempty():
            return self.items[len(self.items) - 1]
        else:
            return None  # Otra opción es lanzar una excepción indicando que la pila está vacía

    def length(self):
        return len(self.items)

    def __str__(self) -> str:
        return self.items.__str__()
