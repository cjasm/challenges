"""
    Reverse only the alphabet characters in a string, keep everything else.
    Example:
        * 'a.b*d' -> 'd.b*a'
        * 'a*b,c@d#eaffeqw)2a*a#31&$*@abe' -> 'e*b,a@a#awqeffa)2e*d#31&$*@cba'
"""


def reverse(s):
    alpha = []
    for char in s:
        if char.isalpha():
            alpha.append(char)

    result = []
    for char in s:
        if char.isalpha():
            result.append(alpha.pop())
        if not char.isalpha():
            result.append(char)

    return ''.join(result)


def reverse(s):
    init = 0
    end = len(s) - 1
    result = list(s)

    while init < end:
        if result[init].isalpha() and result[end].isalpha():
            result[init], result[end] = result[end], result[init]
            init += 1
            end -= 1
        else:
            if not s[init].isalpha():
                init += 1
            if not s[end].isalpha():
                end -= 1
    return ''.join(result)


if __name__ == '__main__':
    s = 'a.b*d'
    assert reverse(s) == 'd.b*a'
    s = 'a*b,c@d#eaffeqw)2a*a#31&$*@abe'
    assert reverse(s) == 'e*b,a@a#awqeffa)2e*d#31&$*@cba'
