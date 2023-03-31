def reverse_non_symbols(text):
    res = ''
    for i in text.split():
        for j in i[::-1]:
            if j.isalpha():
                res += j
    s = dict(enumerate(text))
    for i, j in s.items():
        if j.isalpha():
            s[i] = ''
    c = 0
    for i, j in s.items():
        if j == '':
            s[i] = res[c]
            c += 1
    return ''.join(list(s.values()))

if __name__ == '__main__':
    cases = [
        ('abcd efgh', 'dcba hgfe'),
        ('a1bcd efg!h', 'd1cba hgf!e'),
        ('', '')
    ]

    for text, reversed_text in cases:
        assert reverse_non_symbols(text) == reversed_text