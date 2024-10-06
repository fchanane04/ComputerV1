import sys
import re

def find_degree(equation):
    degree = -1
    for part in equation.split('^'):
        if part and part[0].isdigit():
            current = int(part[0])
            if current > degree:
                degree = current
    return degree

#def check_format(part):
#    print(part)

def check_part_format(part):
    part = part.strip(" \t")
    parts = re.split(r'[+-]', part)
    for part in parts:
        part = part.strip(" \t")
        #check_format(part)

def extract_coeff(part):
    sign = 1
    print("coeff is : ", part)
    if part[0] == "-":
        part = part.strip("-")
        sign = -1
    coeff = float(part) * sign
    return coeff

def extract_power(part):
    part = part[2:]
    print("power is : ", part)
    power = int(part)
    return power

def term_syntax_check(term):
    pattern = r'^-?\d+(\.\d+)?[*]X\^-?\d+$'
    if re.match(pattern, term):
        print("correct format")
        parts = term.split("*")
        coeff = extract_coeff(parts[0])
        print(type(coeff))
        power = extract_power(parts[1])
        print(power)
    else:
        sys.exit("wrong format")


def split_polynomial_terms(expression):
    expression = expression.strip(" \t")
    expression = expression.replace(" ", "")
    expression = expression.replace("-", "+-")
    terms = expression.split("+")
    print("terms are : ", terms)
    for term in terms:
        term_syntax_check(term)

def handle_left_side(expression):
    split_polynomial_terms(expression)

def handle_right_side(expression):
    split_polynomial_terms(expression)

def split_and_check(equation):
    #degree = find_degree(equation)
    parts = equation.split('=')
    if len(parts) != 2:
        print("no more than one =")
    else:
        left_side, right_side = parts
        if not left_side or not right_side:
            print("one of the sides or both is empty")
        else:
            handle_left_side(left_side)
            handle_right_side(right_side)
            for part in parts:
                check_part_format(part)

pairs = set()
lenght = len(sys.argv)

if lenght != 2:
    print("wrong number of arguments")
else:
    if not sys.argv[lenght - 1]: