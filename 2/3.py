

def is_valid_parentheses(s):
    stack = []
    matching_brackets = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in matching_brackets.values():  # Если символ - открывающая скобка
            stack.append(char)
        elif char in matching_brackets.keys():  # Если символ - закрывающая скобка
            if not stack or stack[-1] != matching_brackets[char]:
                return False
            stack.pop()
    return not stack


def longest_valid_substring(s):
    max_length = 0
    start = -1
    stack = []
    st = []

    for i in range(len(s)):
        print(stack,start,max_length)
        st.append(start)
        if s[i] in "({[":
            stack.append(i)
        else:
            if stack:
                stack.pop()
                if not stack:
                    max_length = max(max_length, i + 1)
                    start = 0
                else:
                    max_length = max(max_length, i - stack[-1])
                    start = stack[-1] + 1

    return s[:start + max_length] if max_length > 0 else False


input_string = input("Введите строку: ")

if is_valid_parentheses(input_string):
    print("true")
else:
    result = longest_valid_substring(input_string)

    print(result)