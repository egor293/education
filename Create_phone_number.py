def create_phone_number(n):
    s=''.join(map(str,n))
    return f'({s[:3]}) {s[3:6]}-{s[6:]}'
print(f'+7 {create_phone_number([1,2,3,4,5,6,7,8,9,0])}')
print(f'+7 {create_phone_number([1,1,1,1,1,1,1,1,1,1])}')