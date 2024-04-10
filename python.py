try:
    num = int(input('Enter a number: '))
    num1 = int(input('Enter a digit: '))
    ans = num / num1
except:
    print("Can't dived into zero")
finally:
    print('', ans)
if ans % 2 == 0:
    import login
else:
    print('Invalid')

