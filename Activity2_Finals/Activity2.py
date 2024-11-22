from PositionalList import PositionalList
from LinkedStacked import LinkedStack

def evaluate_postfix(expression):

    stack = LinkedStack()
    operators = {'+', '-', '*', '/'}

    for token in expression.split():
        if token.isdigit():
            stack.push(int(token))
        elif token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2

            stack.push(result)

    return stack.pop()

print()

infix_expr = "(( 5 + 2 ) * ( 8 - 3 )) / 4"
print(f"Current: {infix_expr}")

# Example usage
postfix_expr = "5 2 + 8 3 - * 4 /"
result = evaluate_postfix(postfix_expr)

print(f"Postfix: {postfix_expr}")


print()

numbers = [1, 72, 81, 25, 65, 91, 11]
list = PositionalList()
for num in numbers:
    list.add_last(num)

print(f"Original List: {numbers}")


list.insertion_sort(ascending=True)
ascending_result = list.to_list()
print(f"Ascending order: {ascending_result}")

list.insertion_sort(ascending=False)
descending_result = list.to_list()
print(f"Descending order: {descending_result}")
