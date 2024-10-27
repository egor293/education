def main(cords):
    chessboard={'a':True,'b':False,'c':True,'d':False,'e':True,'f':False,'g':True,'h':False,}
    colors={True:{0:'white',1:'black'},False:{0:'black',1:'white'}}
    a=cords[0].lower()
    b=int(cords[1])
    if chessboard[a]==True:return colors[True][b%2]
    if chessboard[a]==False:return colors[False][b%2]
assert main('e2')=='white',main('e2')
assert main('e8')=='white',main('e8')
assert main('b3')=='white',main('b3')
assert main('h6')=='black',main('h6')