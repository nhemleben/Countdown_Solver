from itertools import combinations
import math
import time
import itertools
from multiprocessing import Pool, cpu_count
from tqdm import tqdm



large_numbers = [25, 50, 75, 100, 25, 50, 75, 100]
small_numbers = [1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,10]


def fix_input(nums):
    '''Return decreasing list of nums'''
    return sorted(nums, reverse=True)

#Example input for function below
    #numbers=[1,2,3,4,5,6]
    #input_items = [(n, str(n)) for n in numbers]
def recurse_generate(items):
    final_candidates = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            (a, ea), (b, eb) = items[i], items[j]
            candidates = []

            candidates.append((a + b, f"({ea} + {eb})"))
            candidates.append((a * b, f"({ea} * {eb})"))

            if a > b:
                candidates.append((a - b, f"({ea} - {eb})"))
            if b > a:
                candidates.append((b - a, f"({eb} - {ea})"))

            if b != 0 and a % b == 0:
                candidates.append((a // b, f"({ea} / {eb})"))
            if a != 0 and b % a == 0:
                candidates.append((b // a, f"({eb} / {ea})"))

            remaining_nums = [items[k] for k in range(len(items)) if k not in (i, j)]
            for val, expr in candidates:
                final_candidates.extend(recurse_generate(remaining_nums+ [(val, expr)]))
            final_candidates.extend(candidates)
    return final_candidates

def mem_efficent_recurse_generate(items):
    final_candidates = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            a,b = items[i], items[j]
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

            remaining_nums = [items[k] for k in range(len(items)) if k not in (i, j)]
            for val in candidates:
                final_candidates.extend(mem_efficent_recurse_generate(remaining_nums+ [val]))
            final_candidates.extend(candidates)
    return final_candidates


def only_valid_final_targets(nums):
    valid_targets = [num for num in nums if num>0 and num%1 ==0]
    return valid_targets

def get_targets(items):
    unique_targets = set()
    for item in items:
        if item[0] not in unique_targets:
            unique_targets.add(item[0])
    return unique_targets

def get_mem_efficent_targets(nums):
    unique_targets = set()
    for num in nums:
        if num not in unique_targets:
            unique_targets.add(num)
    return unique_targets


def generate_countdown_sets(num_large):
    """Generate all valid Countdown starting sets (6-num_large small + num_large large)."""
    large_combos = itertools.combinations(large_numbers, num_large)
    small_combos = itertools.combinations(small_numbers, 6-num_large)
    
    countdown_sets= [tuple(sorted(small + large)) for small, large in itertools.product(small_combos, large_combos)]
    return countdown_sets

def generate_unique_countdown_sets(num_large):
    total_sets = generate_countdown_sets(num_large)
    unique_total_sets = set(total_sets)
    return unique_total_sets


def in_sequence_me_efficent_CDS(unique_total_sets, targets):
    targets = []
    count_completed = 0
    for number_set in unique_total_sets:
        targets.append( mem_efficent_recurse_generate(number_set) )
        count_completed += 1
        if count_completed %10 == 0:
            print(count_completed)
            end_time = time.time()
            running_time = end_time - start_time
            print("Running Execution time:", running_time, "seconds")
            print('average time to complete:', running_time/count_completed)
    return targets




def parallel_solve(all_sets):
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(mem_efficent_recurse_generate, all_sets)
    return results

def parallel_solve_with_progress(all_sets):
    with Pool() as pool:
        for _ in tqdm(
            pool.imap_unordered(mem_efficent_recurse_generate, all_sets, chunksize=50),
            total=len(all_sets)
        ):
            pass


if __name__ == "__main__":

    num_large = 0

    start_time = time.time()

    unique_total_sets = generate_unique_countdown_sets(num_large)
    print(len(unique_total_sets))

    #targets = in_sequence_me_efficent_CDS(unique_total_sets)
    #targets = parallel_solve(unique_total_sets)
    targets = parallel_solve_with_progress(unique_total_sets)

    end_time = time.time()

    print("Total endpoints considered: " +str(len(targets)))
    print("Execution time:", end_time - start_time, "seconds")



#    total_sets = generate_countdown_sets(0)
#    print("Total valid starting sets:", total_sets)
#    print(len(total_sets))
#Upper bound on number of combinations of count down sets
#    a = []
#    for i in range(6):
#        a.append(  math.comb(20,6-i) * math.comb(8,i) )
#    print(sum(a))

#Actual total number of sets
#    a = []
#    for i in range(6):
#        a.append( len(set( generate_countdown_sets(i))) )
#    print(sum(a)) #19373





#



