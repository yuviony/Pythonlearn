#using lists as queue
from collections import deque
queue = deque (["John", "Jack", "James"])
queue.append("Michael")
queue.append("Antony")
print(queue)
print("First to arrive now leaves after queue pop left functions")
queue.popleft()
print(queue)
print("Second to arrive now leaves after queue pop left functions")
queue.popleft()
print(queue)
