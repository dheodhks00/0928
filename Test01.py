a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

d = a + b + c

print(d)

for i in range(len(a)):
    print(a[i], end=" ")
for i in range(len(b)):
    print(b[i], end =" ")
for i in range(len(c)):
    print(c[i], end=" ")

e = [10, 11, 12]
f = [13, 14, 15]
g = [16, 17, 18]

h = e + f+ g

rainbow = ["빨", "주", "노", "초", "파", "남", "보"]
for i in range(len(rainbow)):
    color = rainbow[i]
    print('[{}번째 색은 {}'.format(i+1,color))
