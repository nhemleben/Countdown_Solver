from array import array

def generate_all_2_pair_combos():
    n = 4
    num_reasonable_limit = 10**n +1
    all_reasonable_2_pair_combos = [[array('H') for _ in range(num_reasonable_limit)] for _ in range(num_reasonable_limit)]
    for a in range(1, num_reasonable_limit):
        for b in range(a, num_reasonable_limit): #only need to go from a
            candidates = [ a+b, a*b, ]
            ap = candidates.append
            if a > b: #This streamlines the checks slightly since b%a > 0 in this case
                ap(a - b)
                if a%b ==0: #b can not be zero since I don't let a-b = 0 ever so no need to check
                    ap(a // b)
            elif b > a :
                ap(b-a)
                if b % a == 0:
                    ap(b // a)
            else:
                ap(1) #a/b
            all_reasonable_2_pair_combos[a][b] = candidates
        if a %1000:
            print(a)
    return all_reasonable_2_pair_combos
            
if __name__ == "__main__":
    big_array = generate_all_2_pair_combos()
    print(big_array)