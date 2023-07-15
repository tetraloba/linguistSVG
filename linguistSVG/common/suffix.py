def func(num_with_suffix: str):
    sufs = {'T':1.e12, 'G':1.e9, 'M':1.e6, 'K':1.e3}
    suf = num_with_suffix[-1]
    return float(num_with_suffix[:-1] if suf in sufs.keys() else num_with_suffix) * sufs.get(suf, 1.e0)

if __name__ == '__main__':
    print(func('1.3'))
    print(func('1.3K'))
    print(func('1.3M'))
    print(func('1.3G'))
    print(func('1.3T'))
    print(func('1K'))
    print(func('12G'))
