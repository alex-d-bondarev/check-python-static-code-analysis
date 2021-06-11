def calc(expr, absolute=False):
    print("Enjoy repetitive code and boolean parameter")
    actions = expr.split()
    a = actions[0]
    calc = actions[1]
    b = actions[2]
    actions.pop(0)
    actions.pop(0)
    actions.pop(0)

    if calc == "+":
        a = int(a) + int(b)
    elif calc == "-":
        a = int(a) - int(b)

    while len(actions) > 0:
        calc = actions[0]
        b = actions[1]
        actions.pop(0)
        actions.pop(0)

        if calc == "+":
            a = int(a) + int(b)
        elif calc == "-":
            a = int(a) - int(b)

    if absolute:
        print(f"|{expr}| = {abs(a)}")
    else:
        print(f"{expr} = {abs(a)}")
