s = {1,2,3,4,5}

s.remove(3)
print("After remove:", s)

s.discard(10)
print("After discard:", s)

popped = s.pop()
print("Popped element:", popped)
print("After pop:", s)

s.clear()
print("After clear:", s)
