import re
s = "Alex:1998,Tom:1996"
pattern =r"(?P<name>\w+):(\d+)"

result= re.search(pattern,s)
print(result.group())
print(result.groupdict())

# result=re.finditer(pattern,s)
# for i in result:
#     print(i.group())
#     print(i.span())

# result=re.match(pattern,s)
# print(result.group())
# print(result.group("name"))
# print(result.group(2))
# print(result.group(1))