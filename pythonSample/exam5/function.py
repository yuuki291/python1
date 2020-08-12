# 第五章 関数の利用/作成/ラムダ式

x = abs(-20)
print(x)

data = [10, 20, 30, 40, 50]  # 改行しないprint関数
total = 0
for n in data:
    print(n, end="+")
    total += n
else:
    print("... =", end=" ")
print(total)

str1 = input('整数を入力')
num = int(str1)
total1 = 0
for n in range(num):
    total1 += n
else:
    total1 += num
print(str(num) + 'までの合計は、' + str(total1))


def hello():
    print("Hello!")


hello()


def hello1(name):
    print("Hello, " + name + "!")


hello1("Yuki")
hello1("matuura")


def hello2(name):
    return "Hello" + name + "!"


msg1 = hello2("Taro")
print(msg1)


def hello3(name='noname', age=0):
    print("Hi, I am " + name + "(" + str(age) + ").")


hello3("yuki", 30)
hello3(name="Hanako", age=28)
hello3()


def makeList(*arg):
    deta = {}
    n1 = 0
    total4 = 0
    for num1 in arg:
        deta[n1] = num1
        n1 += 1
        total4 += num1
    else:
        deta['total4'] = total4
        return deta

    deta = makeList(98, 76, 54, 32)
    print(deta)


fn = lambda x, y: print(x * y)

fn(2, 3)
fn(10, 5)
'''

   # 関数の呼び出し(1)
   　　関数名()
   
   # 関数の呼び出し(2)
      関数名(引数1, 引数2,....)
      
# キーワード引数
　　
　　# print関数
       print(値 , end = "\n" , file = sys.stdout , flush = False)
       
   #　値の入力を受け取るinput関数
   　　　input(値)
   
   # 絶対値を得る
   　　　abs(数値)
   
   # 任意の要素を得る
   　　　any(コンテナ)
   
   # 16/8/2進数を得る
   　　　hex(整数)
   　　　oct(整数)
   　　　bin(整数)
   
   # 文字列を評価する
   　　　eval(文字列)
   
   # 合計を得る
   　　　sum(コンテナ)
   
   # 累乗を得る
   　　　pow(整数1, 整数2)
   
   # 小数を丸める
   　　　round(実数)
   
   # 関数定義の基本形(1)
        def 関数名():
            実行する処理
            
   # 関数定義の基本形(2)
        def 関数名(引数用の変数1 ,引数用の変数2 ,...):
            実行する処理
            
   # 戻り値の利用
   　　　def 関数名(変数1, 変数2, ...)
            実行する処理
        return 値
        
   # キーワード引数利用の基本形
   　　  def 関数名(キー = 値1, キー = 値2,...):
   
   # 可変長引数利用の基本形
   　　　def 関数名(*変数):
   
   # ラムダ式の定義
        lambda 引数　: 実行文
'''
