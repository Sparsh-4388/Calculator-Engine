def tokenize(expression):
    tokens = []
    num = ''
    
    for char in expression:
        if char.isdigit() or char == '.':
            num += char

        elif char in '+-/*()':
            if num:
                tokens.append(float(num))
                num = ''
                
            tokens.append(char)

        elif char == ' ':
            continue

        else:
            raise ValueError(f"Invalid expression: {char}")
    
    if num:
        tokens.append(float(num))


    return tokens
        

def multiply_divide(tokens):
    try:
        i = 0
        while i < len(tokens):
            if tokens[i] in ('*','/'):
                left = float(tokens[i - 1])
                right = float(tokens[i + 1])
                
                if tokens[i] == '*':
                    result = left * right
                else:
                    result = left / right

                tokens[i - 1:i + 2] = [result]
                i -= 1
            else:
                i += 1
    except (IndexError, ValueError):
        raise ValueError("Invalid Expression for Multiplication")
        
    return tokens





def add_subtract(tokens):
    try:
        i = 0
        while i < len(tokens):
            if tokens[i] in ('+', '-'):
                left = float(tokens[i - 1])
                right = float(tokens[i + 1])

                if tokens[i] == "+":
                    result = left + right
                else:
                    result = left - right

                tokens[i - 1:i + 2] = [result]
                i -= 1
            else:
                i += 1

    except (IndexError, ValueError):
        raise ValueError("Invalid Expression for Addition")
    
    return result


def brackets(tokens):
    try:
        while '(' in tokens:
            open_idx = None
            for i in range(len(tokens) - 1, -1, -1):
                if tokens[i] == '(':
                    open_idx = i
                    break
            
            close_idx = tokens.index(')', open_idx)
            sub_exp = tokens[open_idx + 1:close_idx]

            result = evaluate(sub_exp)
            tokens[open_idx:close_idx + 1] = [result]
    
    except (IndexError, ValueError):
        raise ValueError("Invalid Expression for Brackets")
    
    return tokens



def evaluate(tokens):
    tokens = multiply_divide(tokens)
    return add_subtract(tokens)            




def main():
    expression = input("Enter an expression: ")
    tokens = tokenize(expression)
    tokens = brackets(tokens)
    result = evaluate(tokens)
    print("Result:", result)


main()