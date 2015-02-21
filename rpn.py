def rpn_eval(expression):
    """
    Evaluate the expression in RPN (Reverse Polish Notation)
    :param expression: Expresseion in RPN (Reverse Polish Notation) to evaluate
    :type expression: str
    :return: Evaluated expression
    :rtype: float
    """

    operator_fn_dct = {
        '+': lambda x, y: x+y,
        '-': lambda x, y: x-y,
        '*': lambda x, y: x*y,
        '/': lambda x, y: x/y,
        '^' : lambda x, y: x**y
    }
    operator_lst = operator_fn_dct.keys()

    stack = []

    for token in expression.split(' '):
        if token in operator_lst:
            second_operand = stack.pop()
            first_operand = stack.pop()
            stack.append(
                operator_fn_dct[token](
                    first_operand,
                    second_operand
                )
            )
        else:
            stack.append(float(token))

    return stack.pop()

if __name__ == '__main__':
    print(rpn_eval('-10 -3 5 - *'))
    print(rpn_eval('3 5 + 10 *'))
    print(rpn_eval('8 2 3 ^ -'))
    print(rpn_eval('8.5 2.5 -'))