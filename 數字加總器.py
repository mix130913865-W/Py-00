input1 = input("輸入一串數字（以空格隔開），算出總和。").split()
output1 = 0
for number in input1:
    output1 += int(number)
print(output1)
