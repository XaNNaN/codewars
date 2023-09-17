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

        pair_permut = {s}
        str_len = len(s)
        for i in range(str_len):
            for y in range(i + 1, str_len):
                pair_permut.add(pair_swap(s, i, y))


        result = s
        return set(result)

    print(pair_permutations(s))

    return list(pair_permutations(s))


permutations('work')
