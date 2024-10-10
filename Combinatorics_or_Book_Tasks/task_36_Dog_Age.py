def dog_age(age):
    if age<0:
        return 'error: wrong age'
    if age>=2:
        return 21+4*(age-2)
    return age*4

assert dog_age(1)==4,dog_age(1)
assert dog_age(-1)=='error: wrong age',dog_age(-1)
assert dog_age(12)==61,dog_age(12)


# Тесты не верные. Может так?
assert dog_age(1)==10.5,dog_age(1)
assert dog_age(2)==21,dog_age(2)
assert dog_age(3)==25,dog_age(3)
    

