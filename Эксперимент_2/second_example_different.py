def example_function(first: str, second: str) -> str:
    try:
        return str(abs(float(first) - float(second)))
    except:
        return "Values are not float"