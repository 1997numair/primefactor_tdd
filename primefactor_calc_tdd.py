def is_prime(PorC):
    for i in range(2,PorC):
        if(PorC % i ==0):
            return False
    return True
def find_primes(user_no):
    if(is_prime(user_no)):
        return user_no
    factor_list=[]
    for i in range(2,user_no):
        if(user_no % i==0):
            factor_list.append(i)
    return factor_list

_primeno_of=4
find_primes(_primeno_of)
print(find_primes(_primeno_of))

