#正则匹配输出字符串
import re
qzw = input()
##  开始  ##
def extract_text_after_bracket(qzw):
    match = re.search(r'\【([^]]+)\】', qzw)
    #match = re.search(r'\[([^]]+)\]', qzw)
    #print(match)
    if match:
        return match.group(1)
    else:
        return '无'
output = extract_text_after_bracket(qzw)
print(output)


#输入  [22]11
#输出  11

#输入  【原文】标记原文内容，用【译文】标记对原文的译文。输出文本前后均无空格。
#输出  标记原文内容，用