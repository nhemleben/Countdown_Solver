import pytest
import math
from itertools import combinations
import CountDown_Solver as CDS


def test_two_numbers():
    numbers = [1,2]
    input_items = [(n, str(n)) for n in numbers]
    targets = CDS.get_targets(CDS.recurse_generate(input_items)) 
    assert len(targets)  ==3
    assert max(targets)  ==3
    assert min(targets)  ==1

def test_two_numbers_mem_efficent():
    numbers = [1,2]
    targets = set(CDS.mem_efficent_recurse_generate(numbers))
    assert len(targets)  ==3
    assert max(targets)  ==3
    assert min(targets)  ==1

def test_parallel_two_numbers_mem_efficent():
    numbers = [1,2]
    numbs, targets = CDS.parallel_mem_efficent_recurse_generate(numbers)
    assert targets[3]  ==1
    assert targets[2]  ==2
    assert targets[1]  ==1

def test_parallel_three_numbers_mem_efficent():
    numbers = [1,2,3]
    numbs, targets = CDS.parallel_mem_efficent_recurse_generate(numbers)
    assert sum(targets) == 48

def test_num_countdown_sets():
    no_large = CDS.generate_countdown_sets(0)
    one_large = CDS.generate_countdown_sets(1)
    assert len(no_large) == math.comb(20,6)
    assert len(one_large) == math.comb(20,5) * math.comb(8,1)

def test_num_countdown_sets_general():
    for i in range(6):
        count_down_set = CDS.generate_countdown_sets(i)
        assert len(count_down_set) == math.comb(20,6-i) * math.comb(8,i)
