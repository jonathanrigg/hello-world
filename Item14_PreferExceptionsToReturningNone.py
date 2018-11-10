def divide(a,b):
    try:
        a/b
    except ZeroDivisionError as e:
        raise ValueError('hi') from e
        #print("kiss my ass")

try:
    divide(2,0)
except ValueError:
    print("invalid Inputs")