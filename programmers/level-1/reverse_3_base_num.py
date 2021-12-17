def base(n,q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]

def solution(n):
    answer = 0
    n_3=base(n,3)
    answer=int(n_3[::-1],3)
    return answer