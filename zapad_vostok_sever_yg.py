def popo(arr):
    b=({
        'NORTH':'SOUTH',
        'SOUTH':'SOUTH',
        'WEST':'EAST',
        'EAST':'WEST'
    })
    for i in range(len(arr)-1):
        if b[arr[i]]==arr[i+1]:
            del arr[i]
            del arr[i]
            return popo(arr)
    return arr
if __name__=='__main__':
    print(popo(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
    print(popo(["NORTH", "WEST", "SOUTH", "EAST",]))


          
