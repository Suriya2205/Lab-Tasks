# Dictionary Task
student = {"name":"John", "age":20, "course": "Python"}
print(student.get("name"))
print(student.keys())
print(student.values())
print(student.items())
student.update({"marks":85})
student.pop("course")
student.popitem()
b = student.copy()
print(b)
student.clear()
print(student)


# Set Task
A = {1,2,3,4}
B = {3,4,5,6}
A.add(7)
A.remove(2)
B.discard(10)
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
A.difference_update(B)
print(A.issubset(B))
print(A.issuperset(B))
print(A.isdisjoint(B))
C = A.copy()
print(C)
B.clear()
print(B)
