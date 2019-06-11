from collections import deque
queue=deque(["AAA","BBB","CCC"])
queue.append("DDD")
print(queue)
queue.popleft()
print(queue)
queue.pop()
print(queue)
