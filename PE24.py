import itertools

nums = '0123456789'

perms = [''.join(p) for p in itertools.permutations(nums)]

print(perms[999999])