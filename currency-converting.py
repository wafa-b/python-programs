dollar_list = []
ryal_list = []

# or  dollar_list = list(range(1,101))

for i in range(1,101):
    dollar_list.append(i)

# print(dollar_list)
converted_rate = float(input("Please enter the converted rate: "))
while True:
    if converted_rate > 0 and converted_rate < 10:
        for i in dollar_list:
            ryal_value = i * converted_rate
            ryal_list.append(ryal_value)
        print('The dollar list is \n',dollar_list)
        print('The ryal list is \n',ryal_list)
        break
    else:
        converted_rate = float(input("The Converted rate should be greater than 0 and less than 10 "))
