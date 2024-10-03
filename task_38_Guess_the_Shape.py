def guess_the_shape(num_of_sides):
    if num_of_sides<3 or num_of_sides>10:
        return 'wrong count of sides'
    a=['Triangle','Tetragon','Pentagon','Hexagon','Heptagon','Octagon','Nonagon','Decagon']
    return a[num_of_sides-3]

assert guess_the_shape(3)=='Triangle',guess_the_shape(3)
assert guess_the_shape(10)=='Decagon',guess_the_shape(10)
assert guess_the_shape(-1)=='wrong count of sides',guess_the_shape(-1)
assert guess_the_shape(9999)=='wrong count of sides',guess_the_shape(9999)

    
