def days_of_month(month):
    months={'January':31,'February':'29/28','March':31,'April':30,'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'December':31}
    if month not in months:
        return 'error: wrong month name, start from capital letter'
    return(months[month])

assert days_of_month('January')==31,days_of_month('January')
assert days_of_month('january')=='error: wrong month name, start from capital letter',days_of_month('january')
assert days_of_month('afdadf')=='error: wrong month name, start from capital letter',days_of_month('afdadf')
assert days_of_month('February')=='29/28',days_of_month('February')