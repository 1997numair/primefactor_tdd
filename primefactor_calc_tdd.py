factor_list=[]
def is_prime(PorC):
    for i in range(2,PorC):
        if(PorC % i ==0):
            return False
    return True
def find_primes(user_no):
    if(is_prime(user_no)):
        factor_list.append(user_no)

    for i in range(2,user_no):
        if(user_no % i==0 ):
            if(is_prime(i)):
                find_primes(i)
                if(product_of(factor_list)<user_no):
                    factor_list.append(i)
            else:
                find_primes(i)
    return factor_list

_primeno_of=8
print(find_primes(_primeno_of))

