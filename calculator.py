#this is pYthon calculator>
def calc(f1,op,s2):
	return eval(f"{f1}{op}{s2}")

f1=int(input("enter 1st no>"))
s2=int(input("enter 2nd no>"))
op=input("enter the operation wanna check:>")
result=calc(f1,op,s2)
print("result",result)

