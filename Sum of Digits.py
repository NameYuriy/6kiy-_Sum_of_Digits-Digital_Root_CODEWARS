def digital_root(n):
    a = [int(x) for x in str(n)]
    count=10
    while count >= 10:
        count = sum(a)
        a=[int(x) for x in str(count)]
    return count