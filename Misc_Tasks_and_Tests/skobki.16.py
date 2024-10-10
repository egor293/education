def main(skobki):
    sa=0
    so=0
    for a in skobki:
        if a =='(':
            sa+=1
        if a ==')':
            so+=1
        if sa<so:
            return False
    return sa==so
skobki=input('pq ')
print(main(skobki))

