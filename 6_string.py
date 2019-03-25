'''문자열 사용하기
""나 ''를 사용해서 문자열 표시
문자열은 여러개의 문자로 이루어져 있기 때문에
반복가능한 자료형
'''

print(dir(str))
'''
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__l
e__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'co
unt', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'l
ower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
'''

'''문자열의 문자 접근하기
색인 연산자([])를 이용해 각 문자에 접근
값은 변경 불가능하다.

string[처음:끝 + 1:간격]
처음과 간격은 지정해주지 않아도된다.
미설정 값은 처음은 0 간격은 1이다.
'''

a = "Hello World!"

print(a[0]) # H
print(a[6]) # W
print(a[5]) # ' '
print(a[-1]) # !
print(a[0:11]) # Hello World
print(a[-2:-1]) # d
print(a[0:11:2]) # HlloWrd

'''문자열 내부 기능
count()   : 문자열 내부 문자 갯수 반환
find()    : 문자의 인덱스 번호를 반환
index()   : 문자의 인덱스 번호를 반환
upper()   : 소문자를 대문자로 변환
lower()   : 대문자를 소문자로 변환
strip()   : 양 끝의 공백 제거
lstrip()  : 왼쪽의 공백 제거
rstrip()  : 오른쪽의 공백 제거
replace() : 문자열의 내용 교체
split()   : 문자열을 나누어줌
'''

a = " aaa bbb ccc "

print(a.count('a')) # 3
print(a.find('a')) # 1
print(a.find('d')) # -1
print(a.index('a')) # 1
# print(a.index('d')) 없는 데이터 검색 시 에러
print(a.upper()) # " AAA BBB CCC "
print(" AAA BBB CCC ".lower()) # " aaa bbb ccc "
print(a.strip()) # "aaa bbb ccc"
print(a.lstrip()) # "aaa bbb ccc "
print(a.rstrip()) # " aaa bbb ccc"
print(a.replace('a', 'd')) # " ddd bbb ccc "
print(a.split()) # ['aaa', 'bbb', 'ccc']
