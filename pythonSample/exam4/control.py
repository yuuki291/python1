# 第四章 制御構文

if True:
    print('if文')


for word in ('python', 'パイソン'):
    print(word)


data = [1, 2, 3, 4]
total = 0
for n in data:
    total += n
ave = total // len(data)
msg = "合計:" + str(total) + "平均:" + str(ave)
print(msg)


data1 = {'国語': 1, '数学': 2, '理科': 3, '体育': 4}
total1 = 0
for k in data1:
    print(k + ":" + str(data1[k]))
    total1 += data1[k]
else:
    print("======データは以上です=======")
ave1 = total1 // len(data1)
msg1 = "合計:" + str(total1) + "平均:" + str(ave1)
print(msg1)


num = 12345
n = 2
res = []
while n <= num // 2:
    if num % n == 0:
        res += [n]
    n += 1
print(str(num) + "の約数")
print(res)


i = [x * 2 for x in range(10) if x % 2 == 0]
print(i)


'''
# if文

if 条件式 :
    処理内容 # Trueの場合
else:
    処理内容 # Falseの場合
elif 条件式3がTrue:
　　処理内容


# for文

for 変数 in コンテナ:
    繰り返す処理
    
for 変数 in コンテナ:
    繰り返す処理
    continue  # continueによる断続
else:
    全データ取得後の処理
    break  # breakによる中断
    

# while文

while 条件式:
     繰り返す処理
     
     
# for文とif文を用いたリスト内包表記
　　　[式　for文 if文]   
'''
