def found(fam,name,fname):
      for x in range(n // fam + 1):
            for y in range(n // name + 1):
                  for z in range(n // fname + 1):
                        if x * fam + y * name + z * fname == n:
                              res = (x, y, z)
                              return 


fam = 11
name = 8
fname = 9

n = int(input())



    
if found(fam,name,fname)[0]:
        print(f'{found[1][0]} фамок + {found[1][1]} имём + {found[1][2]} фнеймов = {n}')
else:
        print('-42')