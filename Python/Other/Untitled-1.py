import re
qzw = input()
#Let's learn Python.
#Let's learn Python. Python is fun.
#【原文】标记原文内容，用【译文】标记对原文的译文。输出文本前后均无空格。
string = qzw
#matchObj = re.match(r'Let\'s', string)
#matchObj = re.search(r'Python', string)
#matchObj = re.search(r'【原文】', string)

#--
#matches = re.findall(r'Python', string)
#matches = re.split(r'\.', string)
matches = re.findall("【原文】(.*)【",string)
#--
#newString = re.sub(r'Python', 'Java', string)
#-----
content_string = ' '.join(matches)
print(content_string)
#--
#if matchObj:
#    print("match Found: ", matchObj.group())
#else:
#    print("No match found")
#--
#print(newString)
#--
#newString, count = re.subn(r'Python', 'Java', string)
 
#print(newString)
#print(count)
#--
#pattern = re.compile(r'Python')
#matchObj = pattern.search('Let\'s learn Python. Python is fun.')

#print(matchObj.group())


