def ntt(num):
    result = ''
    
    if num >= 100000000:
        result += str(num // 100000000) + "억 "
        num %= 100000000
    
    if num >= 10000:
        result += str(num // 10000) + "만 "
        num %= 10000
    
    if num > 0: result += str(num)
    return result.rstrip()