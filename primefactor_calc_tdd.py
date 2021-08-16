def is_prime(PorC):
    for i in range(2,PorC):
        if(PorC % i ==0):
            return False
    return True
def find_primes(user_no):
    if(is_prime(user_no)):
        return user_no
_primeno_of=4
find_primes(_primeno_of)
print(find_primes(_primeno_of))

