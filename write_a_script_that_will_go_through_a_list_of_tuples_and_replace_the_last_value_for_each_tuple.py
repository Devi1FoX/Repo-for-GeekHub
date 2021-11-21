lst = [(10,20,30),(40,50,60,65,30),(70,80,90,20)]
nomer = int(input('Enter some number: '))
new_lst = [tpl[:-1] + (nomer,) for tpl in lst]
print(new_lst)
