input1 = input('Count how many times each word appears in a sentence')
input1 = input1.split()
output1 = {}
for word in input1:
    if word in output1:
        output1[word] += 1
    else:
        output1[word] = 1
print(output1)