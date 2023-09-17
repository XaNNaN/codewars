from math import factorial
import time

def permutations(s) -> list:
    def pair_permutations(s: str) -> set:
        """Returns every swap of two chars in string"""
        def pair_swap(s: str, letter_one: int, letter_two: int) -> str:
            str_len = len(s)
            if str_len - 1 < letter_one or \
                    letter_one < 0 or \
                    str_len - 1 < letter_two or \
                    letter_two < 0:
                raise ValueError("Out of bounds.")

            list_str = list(s)
            tmp = list_str[letter_one]
            list_str[letter_one] = list_str[letter_two]
            list_str[letter_two] = tmp
            return ''.join(list_str)

        pair_permut = set()
        str_len = len(s)
        for i in range(str_len):
            for y in range(i + 1, str_len):
                pair_permut.add(pair_swap(s, i, y))

        return pair_permut

    # print(pair_permutations(s))

    permuts = {s}
    new_permuts = pair_permutations(s)
    permuts = permuts.union(new_permuts)
    while len(new_permuts) > 0:
        roots_permuts = set()
        for root in new_permuts:
            roots_permuts = roots_permuts.union(pair_permutations(root))
        new_permuts = roots_permuts.difference(permuts)
        permuts = permuts.union(new_permuts)


    # print(permuts)
    print(len(permuts), factorial(len(s)))
    return list(pair_permutations(s))

start = time.time()
permutations('механиз')
end = time.time() - start ## собственно время работы программы

print(end) ## вывод времени