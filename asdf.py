while True:
    a = int(input("1~10까지의 숫자 중 하나를 골라보세요 : "))

    if 1 <= a <= 10:
        if a > 5:
            print("큰 숫자")
        else:
            print("작은 숫자")
        break
    
    else:
        print("1~10 사이의 숫자만 입력하세요")