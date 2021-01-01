week=['Sunday','Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday']
a=[]
b=[]
temperature_dict={}
for w in week:
    if w=='Sunday' or w=='Saturday':
        temp=float(input(f"Please Enter temperature for {w}: "))
        a.append(temp)
    else:
        b.append(float(input(f"Please Enter temperature for {w} :")))
try:
    temperature_dict.update({"weekday":(sum(a)/len(a))})
    temperature_dict.update({"weekend":(sum(b)/len(b))})
except:
    print("There is zero division Error")
print(f"Temperature Dictionary \n{temperature_dict}")