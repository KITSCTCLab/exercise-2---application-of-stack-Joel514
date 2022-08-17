class Solution:
   
    def __init__(self, size):
        self.stack = []
        self.queue = []
        self.size = size
        self.top = -1
        self.rear = -1
        self.front = -1

    def is_stack_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def is_queue_empty(self):
        if self.rear == -1 and self.front == -1:
            return True
        else:
            return False

    def is_stack_full(self):
        if self.size == len(self.stack):
            return True
        else:
            return False

    def is_queue_full(self):
        if self.size == len(self.queue):
            return True
        else:
            return False

    def push_character(self, character):
        if not self.is_stack_full():
            self.stack.append(character)
            self.top += 1

    def enqueue_character(self, character):
        if not self.is_queue_full():
            self.queue.append(character)
            self.rear += 1
            if self.front == -1:
                self.front += 1

    def pop_character(self):
        if not self.is_stack_empty():
            data = self.stack.pop()
            self.top -= 1
            return data

    def dequeue_character(self):      
        if not self.is_queue_empty():
            data = self.queue[self.front]
            self.front += 1
            return data

text = input()
length_of_text = len(text)
solution = Solution(length_of_text)

for index in range(length_of_text):
    solution.push_character(text[index])
    solution.enqueue_character(text[index])

is_palindrome = True
for index in range(length_of_text):
    if  solution.pop_character() != solution.dequeue_character():
        is_palindrome = False
        break

if is_palindrome:
    print("The word, " + text + ", is a palindrome.");
else:
    print("The word, " + text + ", is not a palindrome.")
