import unittest


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


class RPNEvaluatorOperationsTestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(rpn_eval('2 3 +'), 5)

    def test_add_with_negatives(self):
        self.assertEqual(rpn_eval('-2 3 +'), 1)
        self.assertEqual(rpn_eval('2 -3 +'), -1)
        self.assertEqual(rpn_eval('-2 -3 +'), -5)

    def test_add_noninteger(self):
        self.assertEqual(rpn_eval('1.23 2.42 +'), 3.65)

    def test_sub(self):
        self.assertEqual(rpn_eval('3 2 -'), 1)

    def test_sub_with_negatives(self):
        self.assertEqual(rpn_eval('2 3 -'), -1)
        self.assertEqual(rpn_eval('-2 3 -'), -5)
        self.assertEqual(rpn_eval('2 -3 -'), 5)
        self.assertEqual(rpn_eval('-2 -3 -'), 1)

    def test_sub_noninteger(self):
        self.assertEqual(rpn_eval('2.42 1.23 -'), 1.19)

    def test_mul(self):
        self.assertEqual(rpn_eval('2 3 *'), 6)

    def test_mul_with_negatives(self):
        self.assertEqual(rpn_eval('-2 3 *'), -6)
        self.assertEqual(rpn_eval('2 -3 *'), -6)
        self.assertEqual(rpn_eval('-2 -3 *'), 6)

    def test_mul_noninteger(self):
        self.assertEqual(rpn_eval('1.23 2.42 *'), 2.9766)

    def test_div(self):
        self.assertEqual(rpn_eval('6 2 /'), 3)

    def test_div_with_negatives(self):
        self.assertEqual(rpn_eval('-6 2 /'), -3)
        self.assertEqual(rpn_eval('6 -2 /'), -3)
        self.assertEqual(rpn_eval('-6 -2 /'), 3)

    def test_div_noninteger(self):
        self.assertEqual(rpn_eval('6.25 2.0 /'), 3.125)

    def test_pow(self):
        self.assertEqual(rpn_eval('2 3 ^'), 8)

    def test_pow_with_negatives(self):
        self.assertEqual(rpn_eval('-2 3 ^'), -8)
        self.assertEqual(rpn_eval('2 -3 ^'), .125)
        self.assertEqual(rpn_eval('-2 -3 ^'), -.125)

    def test_pow_noninteger(self):
        self.assertEqual(rpn_eval('5.0625 .25 ^'), 1.5)

    def test_combined_operations(self):
        self.assertEqual(rpn_eval('2.5 1.75 + 2 ^ 0.0625 - -18 - 36 -'), 0)

if __name__ == '__main__':
    unittest.main()
