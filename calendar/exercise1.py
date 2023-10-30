# import calendar

# yy = int(input("Enter year: "))
# mm = int(input("Enter Month"))

# print (calendar.month(yy,mm))


def transform(a = 2):
    if a == 1:
        return a + 2
    return a

total = 1

for x in [3,5,1]:
    total = total + transform(x)
    print(total)

print(total)