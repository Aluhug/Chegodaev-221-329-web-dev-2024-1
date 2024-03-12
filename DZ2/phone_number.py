def wrapper(f):
    def fun(l):
        dec_nums = []
        for n in l:
            no_pref_num = n[len(n) - 10:]
            dec_num = f"+7 ({no_pref_num[:3]}) {no_pref_num[3:6]}-{no_pref_num[6:8]}-{no_pref_num[8:]}"
            dec_nums.append(dec_num)
        return f(dec_nums)

    return fun

@wrapper
def sort_phone(l):
    return sorted(l)

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    print(*sort_phone(l), sep='\n')
