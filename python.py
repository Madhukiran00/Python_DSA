n=253
string=str(n)

m500=int(string[-3:])//500
m1000=int(string[:-3])
change=int(string[-3:])-500 #750
m100=change//100. #250 2
m50=(change-(m100*100))//50
print(m50)
print("1000s:{0} , 500s:{1} and 100s:{2} ,50s:{3}".format(m1000,m500,m100,m50))







