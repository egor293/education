def binary_search():
    h = 1
    for i in range(200):
        ans = check_answer(h)
        if ans == 'wet':
            h *= 2
            continue
        elif ans == 'ok':
            low = (h // 2) + 1 
            high = h
            mid = (high + low) // 2
            break

    for _ in range(200 - i):
        print(low, high, mid)
        mid = (high + low) // 2
        ans = check_answer(mid)

        if low == high and ans == 'ok':
            return f'! {low}'
        if ans == 'ok':                                                 
            high = mid - 1
            continue
        elif ans == 'wet':
            low = mid + 1
            continue
    return low
        
                
def check_answer(h):
    n = 1023544222
    m = n * 2 + 153454

    if h > m:
        return None
    elif h < n:
        return 'wet'
    elif n <= h < m:
        return 'ok'

print(binary_search())