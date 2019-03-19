class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items

# decimal to binary
def dec_to_bin(dec_num):
    bin_num = ''
    remainder = 0
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2
    while not s.is_empty():
        bin_num += str(s.pop())
    return bin_num

print('\ndecimal to binary')
print('8 :', dec_to_bin(8))
print('115:', dec_to_bin(115))

# string reversal
def str_rev(string1):
    index = 0
    rev_str = ''
    s = Stack()
    while index in range(len(string1)):
        s.push(string1[index])
        index += 1
    while not s.is_empty():
        rev_str += str(s.pop())
    return rev_str

print("\nstring reversal")
print('YOB : ', str_rev("YOB"))
print('NAES : ', str_rev('NAES'))

# parenthesis balance
def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    else:
        return False

def check_paren(string1):
    s = Stack()
    index = 0
    is_Balanced = True

    while index < len(string1) and is_Balanced == True:
        if string1[index] in '([{':
            s.push(string1[index])
        else:
            if s.is_empty():
                is_Balanced = False
                return False
            elif is_match(s.pop(), string1[index]):
                is_Balanced = True
            else:
                is_Balanced = False
                return False
        index += 1
    if s.is_empty() and is_Balanced == True:
        return True
    else:
        return False

print("\nparenthesis checker")
print("([{}])", check_paren("([{}])"))
print("(()", check_paren("(()"))
print("())", check_paren("())"))
print("[]", check_paren("[]"))
print("(([)", check_paren("(([)"))
print("))", check_paren("))"))
