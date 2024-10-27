def main(frequency):
    notes={'c4':261.63,'d4':293.66,'e4':329.63,'f4':349.23,'g4':392.00,'a4':440.00,'b4':493.88}
    for key,value in notes.items():
        if value-frequency>=-1 and value-frequency<=1:
            return key.capitalize()
    return 'wrong frequency'
assert main(261.63)=='C4',main(261.63)
assert main(260.63)=='C4',main(260.63)
assert main(262.63)=='C4',main(259.63)
assert main(251.63)=='wrong frequency',main(251.63)