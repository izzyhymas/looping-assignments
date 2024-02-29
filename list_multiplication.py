def list_multiply_while(a: list[int], b: list[int]) -> list[int]:
    new_list = []
    i = 0

    while i < len(a):
        new_list.append(a[i] * b[i])
        i += 1
    return new_list



def list_multiply_for(a: list[int], b: list[int]) -> list[int]:
    new_list = []

    for i in range(len(a)):
        new_list.append(a[i] * b[i])
    return new_list


def main():

    a = [1, 2, 3]
    b = [4, 5, 6]

    c = list_multiply_while(a, b) # This should compute [1*4, 2*5, 3*6]
    print(c)

    d = list_multiply_for(a, b)
    print(d)

if __name__ == "__main__":
    main()
