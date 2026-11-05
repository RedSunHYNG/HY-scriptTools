import requests
 
# 网址
url = 'https://data.educoder.net/api/attachments/8857916?filesize=131'
 
# 发送HTTP GET请求
response = requests.get(url)
 
# 检查请求是否成功
if response.status_code == 200:
    # 使用StringIO或BytesIO读取内容
    from io import StringIO
    dataset = StringIO(response.text, newline='')
    
    # 处理数据集
    for line in dataset:
        print(line.strip())  # 打印每一行，去除尾部的换行符
else:
    print(f"请求失败，状态码：{response.status_code}")