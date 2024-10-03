popoa=[{
    'arbuz':23424,
    'kal':12,
    'qwdjf':2342,
    'asdl':[1,2,3,{'igra':'letal compani'}]
    }]
# for i,o in popoa.items():
#     print(i,o)
# for i in popoa.keys():
#     print(i)
# for i in popoa.values():
#     print(i)
b=popoa[0]
print(b['arbuz'])
for i,o in b.items():
    print(i,o)
for i in b.keys():
    print(i)
for i in b.values():
    print(i)
print(b['asdl'][3]['igra'])