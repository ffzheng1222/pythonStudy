import json

def python_json():
    # python数据序列化为json数据
    myInfo = [
        {'name': 'tony', 'age': 22, 'flag':False},
        {'name': 'cao', 'age': 24}
    ]
    json_str = json.dumps(myInfo)
    print(type(json_str))
    print(json_str)

def json_python():
    # json数据反序列化
    json_str = '{"name":"tony", "age":22}'
    myInfo = json.loads(json_str)

    print(type(myInfo))
    print(myInfo)


if __name__ == '__name__':
    json_python()
    python_json()