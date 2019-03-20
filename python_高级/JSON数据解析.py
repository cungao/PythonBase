import json


#json.dumps() 对数据进行编码
#json.loads() 对数据进行解码
data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}
print('python dic obj:',type(data))
#将 dic 转化为 str
json_str = json.dumps(data)
print('str json :',type(json_str))

#将 str 转化为 dic
data_dic = json.loads(json_str)
print('loads python dic:',type(data_dic))

#读取 json文件
json_file = open('Demo.json','r',encoding='utf-8')
#data_str = json_file.read()
python_dic = json.load(json_file)
print(python_dic)

#将python dic 写入 json
print_file = open('Test.json','w')
json.dump(data,print_file)
