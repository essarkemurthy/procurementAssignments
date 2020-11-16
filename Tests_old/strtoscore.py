x='21/30'
print(type(x))

y=x.split('/')

scorepercent=int(y[0])/int(y[1])
print(scorepercent)
if scorepercent>=0.07:
    print("Pass")
else:
    print("Fail")