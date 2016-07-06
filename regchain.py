import re
pattern = re.compile('[A-Za-z]+')
st = 'thisIsSpinalTap'
print(re.findall(pattern,st))