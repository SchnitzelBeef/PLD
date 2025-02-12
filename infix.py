infix = input("infix to prefix:\n")

OPS = {"*", "+", "-", "/"}



def calc_prefix(input):
    input = input.strip()
    if input.isdigit():
        return input
    elif input[0] == ('(') and input[-1] == (')'):
        return calc_prefix(input[1:-1])
    else:
        
        i = input.find("(")
        if i != -1:   
            E = input[0:i-1]
            op = input[i-1]
            e = input[i:]
            print("input", input)
            print("E op e", E, op, e)
            e_val = calc_prefix(e)
            E_val = calc_prefix(E)
            return " ".join([op, E_val, e_val])
        else:
            i = len(input)-1
            while i > 0 and input[i] not in OPS:
                i -= 1    
            E = input[0:i]
            op = input[i]
            e = input[i+1:]
            print("input", input)
            print("E op e", E, op, e)
            e_val = calc_prefix(e)
            E_val = calc_prefix(E)
            return " ".join([op, E_val, e_val])
        
        # match (op):
        #     case "+":
        #         return " ".join([op, E_val, e_val])
        #     case "-":
        #         return " ".join([op, E_val, e_val])
        #     case "*":
        #         return " ".join([op, E_val, e_val])
        #     case "/":
        #         return " ".join([op, E_val, e_val])
                

print("Result:", calc_prefix(infix))

(2 + 3 * (4 - 5)) * 6 / 7
