import re

line = "Cats are smarter than dogs"
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
if searchObj:
   print("searchObj.group() : ", searchObj.group())
   print("searchObj.group(1) : ", searchObj.group(1))
   print("searchObj.group(2) : ", searchObj.group(2))
else:
   print("Nothing found!!")


line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
   print("matchObj.group() : ", matchObj.group())
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(2) : ", matchObj.group(2))
else:
   print("No match!!")


phone = "2004-959-559 # This is Phone Number"
num = re.sub(r'#.*$', "", phone)
print("Phone Num : ", num)
num = re.sub(r'\D', "", phone)
print("Phone Num : ", num)



line = "origin/HEAD -> origin/master"
matchObj = re.match(r'origin/HEAD\s+->\s+.*', line, re.M | re.I)
if matchObj:
   print("Touhid")
   print(matchObj.group())
   print(re.sub(r'origin/HEAD\s+->\s+origin/', '', line))
