def greet(message, who, sure):
    if sure:
        print(message,who)
    return len(message) + len(who) + 1
    print("I hate Mr. Gunn")

a = greet("hey","guys",True)
b = greet("hi","guys",False)
c = greet("yo","girls",True)
print(a,b,c)
