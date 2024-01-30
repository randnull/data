def func(first, second):
    try:
        float(first)
    except:
        return "First value are not float"

    try:
        float(second)
    except:
        return "Second value are not float"

    float_first = float(first)
    float_second = float(second)

    if abs(float_first - float_second) < 0.00001:
        return "Values different less than 0.00001"

    if abs(float_first - float_second) < 0.001:
        return "Values are different more than 0.00001 but less than 0.001"
    
    return "Values are different more than 0.001"