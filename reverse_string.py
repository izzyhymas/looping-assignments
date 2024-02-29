def reverse_while(s: str):
    new_string = ""
    i = len(s) -1

    while i >= 0:
        new_string += s[i]
        i -= 1
    return new_string

def reverse_for(s: str):
    new_string = ""
    
    for i in range(len(s)-1, -1, -1):
        new_string += s[i]
    return new_string

def reverse_foreach(s: str):
    new_string = ""

    for char in s[::-1]:
        new_string += char
    return new_string


def main():
    s = "hello"

    r = reverse_for(s)

    print(r)

if __name__ == "__main__":
    main()
