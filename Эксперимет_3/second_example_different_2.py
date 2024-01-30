def func(first, second):
    if not first.isdigit():
        return "first is not digit"
    
    if not second.isdigit():
        return "second is not digit"

    if int(first) - int(second) < 0:
        return -(int(first) - int(second))
    return int(first) - int(second)

