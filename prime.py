# if the number is prime or not

def is_prime(number):
    for i in range(2, number):
        if (number % i == 0):
            print("Not a Prime")
            break
    else:
        print("Is a Prime")

is_prime(5)
is_prime(11)
is_prime(55)
is_prime(43)
is_prime(81)