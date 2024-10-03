def dog_age(age):
    if age<0:
        return 'error: wrong age'
    if age>=2:
        return 21+4*(age-2)
    return age*4

assert dog_age(1)==4,dog_age(1)
assert dog_age(-1)=='error: wrong age',dog_age(-1)
assert dog_age(12)==61,dog_age(12)
    

