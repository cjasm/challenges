def starts_with_B_and_ends_with_A(word):
    return word.startswith('B') and word.endswith('A')


if __name__ == '__main__':
    assert starts_with_B_and_ends_with_A('BARCA')
    assert not starts_with_B_and_ends_with_A('Barca')
    assert not starts_with_B_and_ends_with_A('CABANA')
    assert starts_with_B_and_ends_with_A('BACANA')
    assert starts_with_B_and_ends_with_A('BANANA')
