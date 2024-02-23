def summation_while(n):
    total = 0
    i = 1

    while i <= n:
        total += i
        i += 1
    return total

def summation_for(n):
    total = 0
    i = 1

    for i in range(i, n + 1):
        total += i
    return total

def main():
    n = 10

    print(summation_while(n))
    print(summation_for(n))

if __name__ == "__main__":
    main()
