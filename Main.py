import operator
class Evaluate:
  """This class validates and evaluate postfix expression.
  Attributes:
      top: An integer which denotes the index of the element at the top of the stack currently.
      size_of_stack: An integer which represents the size of stack.
      stack: A List which acts as a Stack.
  """
    # Write your code here


  def __init__(self, size):
    """Inits Evaluate with top, size_of_stack and stack.
    Arguments:
      size_of_stack: An integer to set the size of stack.
    """
    self.top = -1
    self.size_of_stack = size
    self.stack = []


  def isEmpty(self):
    """
    Check whether the stack is empty.
    Returns:
      True if it is empty, else returns False.
    """
      # Write your code here
    if len(self.stack)==0:
        return True
    else:
        return False


  def _pop(self):
    """
    Do pop operation if the stack is not empty.
    Returns:
      The data which is popped out if the stack is not empty.
    """
    # Write your code here
    if self.isEmpty():
      print("Your stack is empty")
    else:
        return self.stack.pop()


  def push(self, operand):
    """
    Push the operand to stack if the stack is not full.
    Arguments:
      operand: The operand to be pushed.
    """
    # Write your code here
    self.operand = operand
    if len(self.stack)==self.size_of_stack:
      print("Your stack is full")
    else:
        self.stack.append(self.operand)
        self.top+=1
       


  def validate_postfix_expression(self, expression):
    """
    Check whether the expression is a valid postfix expression.
    Arguments:
      expression: A String which represents the expression to be validated.
    Returns:
      True if the expression is valid, else returns False.
    """
    for x in expression:
        if x.isnumeric()==True:
            return True
        else:
            if x=="+" or x=="-" or x=="" or x=="/" or x=="*":
                return True
            else:
                return False
   


  def evaluate_postfix_expression(self, expression):
    """
    Evaluate the postfix expression
    Arguments:
      expression: A String which represents the the expression to be evaluated
    Returns:
      The result of evaluated postfix expression.
    """
    for i in expression:
        if i.isnumeric():
            self.push(int(i))
        else:
           a=self._pop()
           b=self._pop()
           operations_dictionary={"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.floordiv,"^":operator.pow}
           self.push(operations_dictionary[i](b,a))
     
    return self.stack[0]


# Do not change the following code
postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')
