
"""
lower = 10
upper = 100
lower =int(input("Enter a lower number({}---{}):".format(lower,upper)).strip())
upper =int(input("Enter a upper number({}---{}):".format(lower,upper)).strip())

for i in range(lower , upper):
    print("{} {}".format(i, chr(i)))
"""

def get_number():
    lower =int(input("Enter a lower number: "))
    upper =int(input("Enter a upper number: "))
    while True:
        if upper > lower:
            break
        print("upper value too low!")
        upper =int(input("Enter a upper number: "))
    return lower,upper


def main():
    lower,upper = get_number()
    for i in range(lower , upper):
        print("{} {}".format(i, chr(i)))

main()