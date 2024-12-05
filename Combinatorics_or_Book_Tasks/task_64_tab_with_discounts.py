from tabulate import tabulate
def main(prices,discount):
    ans={}
    for i,price in enumerate(prices):
        ans[f'${price}']=f'${round(price*(discount/100),2)}'
    return ans,print(tabulate(ans.items(), headers=['STANDART', 'DISCOUNT'], tablefmt="grid"))

print(main(prices=[4.95,9.95,14.95,19.95,24.95],discount=60))
assert(main(prices=[4.95,9.95,14.95,19.95,24.95],discount=60))==({'$4.95': '$2.97', '$9.95': '$5.97', '$14.95': '$8.97', '$19.95': '$11.97', '$24.95': '$14.97'}, None),main(prices=[4.95,9.95,14.95,19.95,24.95],discount=60)



