$ cat fizbuz2
def fiz_buz():

  for m in range(1,101):
    if m%3 ==0  and m%5 ==0:
      print(f"{m} FIZZBUZZ")
    elif  m%3 ==0 :
        print(m,"  FIZZ")
    elif  m%5 ==0:
        print(m,"  BUZZ")
    else:
        print("{}  NEITHER".format(m))

fiz_buz()

