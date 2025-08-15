num = "2300019"
cro = "-1"
z = num[:-2]
for i,a in enumerate(z):
    if num[i] == num[i+1] == num[i+2]:
        cro = str(max(int(cro),int(num[i] + num[i+1] + num[i+2])))
if cro == "-1" : return ""
if cro == "0" : return "000"
return(cro)