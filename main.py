from queue import Queue
from collections import deque
import numpy as np

queue = Queue()

def generate_request():
    request_id = np.random.randint(0, 100)
    queue.put(request_id)
    return f"Створено заявку під номером {request_id}"

def process_request():
    if not queue.empty():
        return f"Обробка заявки під номером {queue.get()}"
    else:
        return "Черга пуста"

def palindrome(str: str) -> str:
    dq = deque()
    [dq.append(x) for x in "".join(str.lower())]
    while dq:
        if len(dq) == 1:
            break
        right = dq.pop()
        left = dq.popleft()
        if right != left:
            return False
    return True

print("Згенерувати заявку: '1';\nОпрацювати заявку: '2';\nПеревірити поліндром: str;\nВийти з програми: 'exit'\n")
while True:
    command = input()
    if command == "1":
        print(generate_request())
    elif command == "2":
        print(process_request())
    elif command == "exit":
        break
    else:
        print(palindrome(command))