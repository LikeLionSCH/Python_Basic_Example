'''리스트 사용하기
[]을 사용해 리스트를 선언하거나
list() 함수를 사용해 리스트를 선언할 수 있다.
'''

print(dir(list))
'''
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass
__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append',
'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''

'''리스트 내부 기능
append()  : 리스트에 데이터를 삽입
count()   : 리스트 안의 데이터의 개수를 반환
extend()  : 리스트에 데이터를 삽입
insert()  : 리스트에 데이터를 삽입
pop()     : 리스트에 데이터를 삭제
remove()  : 리스트에 데이터를 삭제
reverse() : 리스트를 거꾸로 변환
sort()    : 리스트를 정렬
'''

a = [1, 2, 3, 4, 5, 6]

a.append(7)
print(a) # [1, 2, 3, 4, 5, 6, 7]

print(a.count(7)) # 1

a.extend([8, 9, 10])
print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a.append([11, 12, 13])
print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12, 13]]

a.insert(0, "new data")
print(a) # ['new data', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12, 13]]

print(a.index(1)) # 1
# print(a.index(14))

print(a.pop()) # [11, 12, 13]
print(a) # ['new data', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a.remove(10)
print(a) # ['new data', 1, 2, 3, 4, 5, 6, 7, 8, 9]

a.reverse()
print(a) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 'new data']

a = [1, 3, 2, 4, 5, 6, 10, 9, 8]
a.sort()
print(a) # [1, 2, 3, 4, 5, 6, 8, 9, 10]

'''리스트의 각 데이터에 접근하기
문자열과 같이 [] 연산자를 사용해 접근할 수 있다.
len() : 데이터의 개수를 반환

list[처음:끝 + 1:간격]
처음과 간격은 지정해주지 않아도된다.
미설정 값은 처음은 0 간격은 1이다.
'''

arr = [x for x in range(10)]

print(arr) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(arr[0]) # 0
print(arr[-1]) # 9
print(arr[0:len(arr)]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr[0:len(arr):2]) # [0, 2, 4, 6, 8]
