"""
Given an expression string, write a python program to find whether a given string has balanced parentheses or not.

Examples:

Input : {[]{()}}
Output : Balanced

Input : [{}{}(]
Output : Unbalanced

One approach to check balanced parentheses is to use stack.
1.Each time, when an open parentheses is encountered push it in the stack.

2.When closed parenthesis is encountered, match it with the top of stack and pop it.

3.If stack is empty at the end, return Balanced otherwise, Unbalanced.

"""

def check_parenthesis(mystr, n):
    open_list = ['[', '{', '(']
    close_list = [']', '}', ')']

    
    stack = []
    for i in range(n):
        if mystr[i] in open_list:
            stack.append(mystr[i])
        elif mystr[i] in close_list:
            pos = close_list.index(mystr[i])
            if len(stack) > 0 and open_list[pos] == stack[-1]:
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"

def check_parenthesis2(mystr, n):
    d = {'(': ')', '[' :']', '{': '}'}
    stack = []
    for i in mystr:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        elif i == ')' or i == ']' or i == '}':
            value = stack.pop()
            if d[value] != i:
                return "Unbalanced"
            else:
                continue
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"

def check_parenthesis3(mystr, n):
    stack = []
    for char in mystr:
        if char in ['(', '[', '{']:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ')':
                    return False
                if current_char == '[':
                    if char != ']':
                        return False
                if current_char == '{':
                    if char != '}':
                        return False
    if stack:
        return False
    return True



"""
Approach#2 : Elimination based:-

In every iteration, the innermost brackets get eliminated (replaced with empty string).
If we end up with an empty string, our initial one was balanced; otherwise, not.

"""

def check_parenthesis_elem(mystr, n):
    brackets = ['()', '{}', '[]']
    for s in mystr:
        for br in brackets:
            if br in mystr:
                mystr = mystr.replace(br, '')
    if len(mystr) == 0:
        return "Balanced"
    else:
        return "Unbalanced"

string = "{[]{()}}"
print(string,"-", check_parenthesis(string, len(string)))

string = "[{}{})(]"
print(string,"-", check_parenthesis(string, len(string)))

string = "{[]{()}}"
print(string,"-", check_parenthesis_elem(string, len(string)))

string = "[{}{})(]"
print(string,"-", check_parenthesis_elem(string, len(string))) 
    
