
def sound_volume(volume):
    if volume>130 or volume<40:
        return -1
    volumes={130:'Отбойный молоток',
             106:'Газовая газонокосилка',
             70:'Будильник',
             40:'Тихая комната'}   
    a=sorted([130,106,70,40,volume])
    for i in volumes.keys():
        if volume==i:
            return volumes[volume]
    return f'{volumes[a[a.index(volume)-1]]} or {volumes[a[a.index(volume)+1]]}'

assert sound_volume(130)=='Отбойный молоток',sound_volume(130)
assert sound_volume(100)=='Будильник or Газовая газонокосилка',sound_volume(100)










 