# 第二章 基本データ/変数/演算/文の書き方

a = 100  # スペースは任意
A = 100
c = a + A
print(a)
print(A)
print(c)


'''
   大文字と小文字は別の文字
   
# 基本となるデータのための型
   int (整数)　... 1      #n進数　: 123,-100000000,0x2A1C,0b10001101
   float (実数) ...1.0    #浮動小数点数　: 仮数がおよそ15~17桁程度増える
   bool (真偽値) ...True
   str (文字列) ..."文字列(テキスト)"

# 複雑なデータなどのための型   
   tuple (タブル(データのまとまり)) ... ('A', 1)
   bytes (ASCⅡ(英数字と一部の記号)のみの特殊な文字列) ... b'Japan'
   list (リスト(データのまとまり)) ... [100,200,300]
   bytearray (ASCⅡ文字のまとまり) ... bytearray(200)
   range (数のシーケンス) ... range(10)
   dict (辞書(データのまとまり)) ... {'skill': 100, 'name': 'yuki'}
   
# 特殊な型
  NoneType (値が存在しないことを表す) ...None
  NotImplementedType (ある型に対して演算が実装されていないことを表す) ...NotImplemented
  Ellipsis (一部の構文で使われる特殊な値)　... ...
  complex (複素数) ...3j
  builtin_function_or_method (組み込み関数/メソッド) ... print
  
# その他の型
  function (関数) ... 自分で定義した関数
  type (型)　... int

※　予約語は使えない

・キャスト可能(強制的に変数の型を変える)

A(1) and B(0) ...掛け算  #論理積
A(1) or B(0) ...足し算　　#論理和
not A ... not演算   #TrueがFalseになる

# ビット単位演算
    1010 & 1100    # 1000
    1010 | 1100    # 1110
    1010 ^ 1100    # 0110
    
・フォーマット済みの文字列リテラルを出力可能

         ssg = "df"
         feg = "vfb"
    例　　print("fsf {ssg}.I'm {feg} sds")
'''




