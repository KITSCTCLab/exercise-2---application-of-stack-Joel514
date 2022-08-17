import operator
class Evaluate:

  def __init__(self, size):
    self.top = -1
    self.size_of_stack = size
    self.stack = []

  def isEmpty(self):
        if len(self.stack)==0:
        return True
    else:
        return False

  def _pop(self):
    if self.isEmpty():
      print("Your stack is empty")
    else:
        return self.stack.pop()

  def push(self, operand):
    self.operand = operand
    if len(self.stack)==self.size_of_stack:
      print("Your stack is full")
    else:
        self.stack.append(self.operand)
        self.top+=1
       

  def validate_postfix_expression(self, expression):
    for x in expression:
        if x.isnumeric()==True:
            return True
        else:
            if x=="+" or x=="-" or x=="" or x=="/" or x=="*":
                return True
            else:
                return False

  def evaluate_postfix_expression(self, expression):
    for i in expression:
        if i.isnumeric():
            self.push(int(i))
        else:
           a=self._pop()
           b=self._pop()
           operations_dictionary={"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.floordiv,"^":operator.pow}
           self.push(operations_dictionary[i](b,a))
     
    return self.stack[0]

postfix_expression = input()  
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')
