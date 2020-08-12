# 第五章 クラスの作成/インスタンスの作成/メソッドの利用/継承

class MyObj:
    pass


ob = MyObj()
print(type(ob))


# メモクラス (Memo)を作成する
class Memo:
    message = "OK"


memo = Memo()
print(memo.message)
memo.message = "Hello!"
print(memo.message)


class MyClass:
    message = "OK"

    # print関数とは別にここではprintメソッドを定義する
    def print(self):  # selfでなくても大丈夫
        print(self.message)


ob1 = MyClass()
ob1.message = "Hello Python!"
ob1.print()


class MyYou:
    def __init__(self, msg):
        self.message = msg

    def print(self):
        print(self.message)


ob2 = MyYou('Hello!')
ob2.print()


class MyMe:
    def __init__(self):
        self.__num = 123  # プライベート変数だからインスタンスでのアクセスができない
        self.message = 'OK!'

    def print(self):
        print(str(self.__num) + 'num' + self.message)


ob4 = MyMe()
ob5 = MyMe()
ob5.__num = 321  # プライベート変数は変更されない -> 出力後 123のまま
ob4.message = 'Hi!'
ob4.print()
ob5.print()


class MyMe:
    message = "OK!"

    @classmethod
    def print(cls):
        print(cls.message)


MyMe.print()  # クラスメソッドは、クラスから直接呼び出して実行できる
MyMe.message = 'Welcome'
MyMe.print()


class Str:
    def __init__(self, msg):
        self.message = msg

    def print(self):
        print(self.message)

    def __str__(self):
        return "<Str: message='>" + self.message + "'>"


ob7 = Str('Hi!you')
print(ob7)


class Person:
    name = "name"


class Human(Person):
    age = 20


ob10 = Person()
print(ob10.name)
ob9 = Human()
print(ob10.name + ',' + str(ob9.age))
'''

   # クラスの定義
   　　　class クラス名 :
             クラスの内容
   
   # インスタンスの作成
        クラス名() 
        
   # クラス変数のクラス内での定義
   　　　class クラス名 :
              変数 = 値
              
   # 値を取り出す
   　　　インスタンス.変数
   
   # 値を変更する
   　　　インスタンス.変数 = 値
   
   # メソッドの利用
   　　　class クラス名:
              def メソッド名(self, 引数):
                   --------実行文--------
                   
　　# 初期化のメソッド
　　　　　def __init__(self):
            ---------初期化処理--------
            
    # プライベート変数
        __変数名 = 値
        
    # クラス変数へのアクセス
    　　クラス.変数
    
    # クラスメソッドの書き方
       @classmethod
       def メソッド名(cls, 引数1, 引数2,...):
       
    # 演算子のための演算メソッド{
    
       # +演算子
          __add__(self, other)
          
       # +=演算子
          __iadd__(self, other)
          
       # -演算子
          __sub__(self, other)
          
       # -=演算子
          __isub__(self, other)
          
       # *演算子
          __mul__(self, other)
          
       # *=演算子
          __isul__(self, other)
          
       # /演算子
          __truediv__(self, other)
          
       # /=演算子
          __itruediv__(self, other)
          
       # //演算子
          __floordiv__(self, other)
          
       # //=演算子
          __ifloordiv__(self, other)
          
       # %演算子
          __mod__(self, other)
          
       # %=演算子
          __imod__(self, other)
          
    }
    
    # 文字列として取り出す動作を定義する
         def__str__(self):
            return 文字列
    
    # プロパティの定義
    　　　@property
           def プロパティ名(self):
               return 値
               
    # プロパティ名.setter
       def プロパティ名(self, 値):
       ---------値を設定する処理------
       
    # 継承するクラスの定義
    　　　class クラス名(継承クラス):
           -----実行中-----
       
'''
