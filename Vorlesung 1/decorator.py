# Decorator

def f1(func):
    def wrapper(*args, **kwargs):
        print("Start")
        func(*args, **kwargs)
        print("Stop")
    return wrapper


@f1  # Ist gleichbedeutend mit f = f1(f)
def f(name):
    print("Hallo", name)


f("Studierende")
