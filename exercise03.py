import re
s = "Alex:1998,Tom:1996"
res= r"\w+:\d+"
res1=r"(\w+):(\d+)"
print(re.findall(res,s))
print(re.findall(res1,s))
list_=re.split(r"\W+",s)
print(list_)
