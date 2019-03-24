'''딕셔너리 생성하기
변수 이름 = {}
기본 값을 설정 가능하다.

변수 이름 = dict()
비어있는 딕셔너리만 생성 가능하다.
'''

dic = {
    "a": "apple",
    "b": "banana",
    "c": "cake",
}

print(type(dic)) # <class 'dict'>
print(dic) # {'a': 'apple', 'b': 'banana', 'c': 'cake'}

dic = dict()

print(dic) # {}

# dic = dict(
#   "a": "apple",
#   "b": "banana",
#   "c": "cake",
# )

'''딕셔너리에 값 삽입하기
dic[key] = val

중복된 키는 가장 나중에 삽입된 데이터로 저장
'''

dic["d"] = "example"

print(dic) #  {'d': 'example'}

dic["d"] = 9

print(dic) # {'d': 9}

'''딕셔너리의 값에 접근하기
dic[key]의 형태로 접근
'''

dic = {
    "a": "apple",
    "b": "banana",
    "c": "cake",
}

print(dic["a"]) # apple
print(dic["c"]) # cake
# print(dic["d"])

'''딕셔너리 내부 기능
keys()   : 딕셔너리의 모든 키를 반환
values() : 딕셔너리의 모든 값을 반환
items()  : 딕셔너리의 모든 키, 값을 반환
get()    : 딕셔너리의 찾고자하는 값을 반환
pop()    : 딕셔너리의 값을 삭제
'''

dic = {
    "a": "apple",
    "b": "banana",
    "c": "cake",
    "d": 9,
}

print(dic.keys()) # dict_keys(['a', 'b', 'c', 'd'])
print(dic.values()) # dict_values(['apple', 'banana', 'cake', 9])
print(dic.items()) # dict_items([('a', 'apple'), ('b', 'banana'), ('c', 'cake'), ('d', 9)])
print(dic.get('a')) # apple
print(dic.get('f')) # None
print(dic.get('f', 'No Data')) # No Data
print(dic.pop('d')) # 9
print(dic) # {'a': 'apple', 'b': 'banana', 'c': 'cake'}
