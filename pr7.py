chatp=int(input())
gr=[]
dog=0
for h in range (0,chatp+1):
    dog=abs((2**h)-chatp)
    gr.append(dog)
kall=min(gr)
print(kall)
