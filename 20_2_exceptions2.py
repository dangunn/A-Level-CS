def fix_gramar(s):
    if s.lower() == "i hate mr. gunn":
        raise RuntimeError("You're suspended.")
    return s[0].upper() + s[1:] + "."

try:
    line = input("Enter a line to punctuate:")
    line2 = fix_gramar(line)
    print(line2)
except IndexError:
    print("No blank lines allowed")
    print(1/0)
except AttributeError:
    print("Must be called with a string")
except Exception as e:
    print(e)
finally:
    print("-- Copyright Daniel Gunn")