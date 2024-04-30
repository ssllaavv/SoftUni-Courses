def calculate(expression: str):
    corrected_expression = expression.replace("^", "**")
    result = eval(corrected_expression)
    print(f"{result:.2f}")

