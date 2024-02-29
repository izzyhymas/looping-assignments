def char_count_while(target: str, c: str): 
    count = 0
    i = 0

    while i < len(target):
        if target[i] == c:
           count += 1
        i += 1
    return count


def char_count_for(target: str, c: str):
    count = 0

    for i in range(len(target)):
        if target[i] == c:
            count += 1
    return count


def char_count_foreach(target: str, c: str):
    count = 0

    for char in target:
        if char == c:
            count += 1
    return count


def main():
    s = "hello"
    c = "l"

    num_times_c_in_s = char_count_foreach(s, c)

    print(num_times_c_in_s)

if __name__ == "__main__":
    main()
