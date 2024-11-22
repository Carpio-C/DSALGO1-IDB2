from ArrayStack import ArrayStack as Stack


def Act3(symbols):

    matching_pairs = {')': '(', '}': '{', ']': '['}

    stack = []

    for symbol in symbols:
        if symbol in matching_pairs.values():
            stack.append(symbol)
        elif symbol in matching_pairs.keys():
            if stack == [] or stack.pop() != matching_pairs[symbol]:
                return False

    return stack == []



user_input = input("Enter symbols: ")

if Act3(user_input):
    print("Correct")
else:
    print("Incorrect")

def reverse_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    reversed_content = content[::-1]
    with open(filename, 'w') as file:
        file.write(reversed_content)
    print('Reverse:')
    print(reversed_content)
reverse_file('myfile.txt')
