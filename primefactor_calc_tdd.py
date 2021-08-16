factor_list=[]
_primeno_of=8
def product_of(list_product):
    p=1
    for i in range(0,len(list_product)):
        p=p*list_product[i]
    return p

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
                if (product_of(factor_list)*i <= _primeno_of):
                    find_primes(i)
                    factor_list.append(i)
            else:
                if(product_of(factor_list)*i <=_primeno_of):
                    find_primes(i)
    return factor_list


print(find_primes(_primeno_of))

