def longest_substring_with_k_distinct(s: str, k: int) -> str:
    if k == 0 or not s:
        return " "

    char_count = {}
    max_len = 0
    max_substr = ""
    window_start = 0

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char not in char_count:
            char_count[right_char] = 0
        char_count[right_char] += 1

        while len(char_count) > k:
            left_char = s[window_start]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            window_start += 1

        if window_end - window_start + 1 > max_len:
            max_len = window_end - window_start + 1
            max_substr = s[window_start:window_end + 1]

    return max_substr
s = "MAMBA"
k = 2
print(longest_substring_with_k_distinct(s, k)) 
