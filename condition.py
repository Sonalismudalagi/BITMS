l=int(input("Enter the number of lemons:"))
print('extra by {}'.format(l-21) if l>21 else 'less by {}'.format(21-l) if l<21 else 'sufficient')

