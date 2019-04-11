num = int(input("숫자를 입력 하세요 : "))

if num == 0:
    print("0은 양수도 음수도 아닙니다.")

elif num > 0:
    print("{}은 양수입니다.".format(num))

else:
    print("{}은 음수입니다.".format(num))
