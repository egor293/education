def main(note):
    notes={'c':261.63,'d':293.66,'e':329.63,'f':349.23,'g':392.00,'a':440.00,'b':493.88}
    a=note[0].lower()
    b=float(note[1])
    return notes[a]/(2**(4-b))

assert main('C4')==261.63,main('C4')
assert main('b4')==493.88,main('b4')
assert main('E7')==2637.04,main('E7')