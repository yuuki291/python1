# 第三章 リスト/タブルとレンジ/セット/辞書

x = {1, 2, 3, 4, 5, 6}  # (ミュータブル)
print(x)

x = [1, 2, 3]  # (ミュータブル)
x[1] = 5  # 配列[1]が5に上書きされる
print(x)

arr = [10, 20, 30, 40]
arr[0] = arr[1] + arr[2] + arr[3]
print(arr)

visitor = []
visitA = '男性'
visitB = '女性'
visitC = '男性'
visitor += [visitA] + [visitB] + [visitC]
print(visitor)

list1 = [10, 20, 30]
var = 10 in list1  # シーケンス
print(var)

list2 = [10, 20, 30]
var2 = 10 not in list1  # シーケンス
print(var2)

arr1 = [10, 20, 30, 40, 50]
var3 = arr1[1:4]  # 配列1から4までを出力
print(var3)

arr4 = [1, 2, 3, 4]
var5 = len(arr4)  # len <-> max <-> min に変える
print(var5)

arr6 = [1, 2, 3, 4]
arr6.insert(1, 1000)  # insert <-> remove <-> pop <-> clear <-> reverse <-> sortに変える
print(arr6)

arr7 = [1, 2, 3, 4, 5, 6]
del arr7[1]
print(arr7)

tp = (10, 'a', True)  # タプル　(イミュータブル) -> いくつかの値をセットにして扱うためのコンテナ
tp1 = tp[0:3]
print(tp1)

rg = range(10, 20, 2)
i = rg[0]
w = rg[1]
c = rg[2]
print(i + w + c)

list3 = [100, 200, 300]
tpl4 = (123, 'ok', True)
run1 = range(10, 20)
result = list3 + list(tpl4) + list(run1)
print(result)

'''

# シーケンス演算 {

   # 要素数を得る
   　　　len(リスト)
   
   # 最小値を得る
   　　　min(リスト)
   
   # 最大値を得る
        max(リスト)
   }
   
        
   # リストの指定位置に値を追加
   　　リスト.insert(インデント , 値)
   
   # リストから値を削除する
   　　リスト.remove(値)
   
   # 最後の値を削除する(取り出す)
      リスト.pop()
      
   # リストのクリア
   　　リスト.clear()
   
   # リストの並びを反転させる
   　　リスト.reverse()
   
   # リストの並べ替え
   　　リスト.sort()
       リスト.sort(reverse = 真偽値)
   
   # 指定したオブジェクトを削除する
   　　del オブジェクト
   
   #　タプルの注意点
       イミュータブルであること(値の変更が不可能なもの)
       ...配列はミュータブル(値の変更が可能なもの)
       
       ・演算は可能
       
   # 範囲を表すレンジ {
        # ゼロから指定の値までのレンジ
        　　　　range(終了値)
        
        # 指定した範囲のレンジ
        　　　　range(開始値 , 終了値)
        
        # 一定間隔のレンジ
        　　　　range(開始値 , 終了値 , ステップ)
            
         ・シーケンス演算可能
    }
    
     # シーケンス間の変換      
     
        # リストに変換する
               list(値)
               
        # タプルに変換する
               tuple(値)
        
        # レンジに変換する
        　　　　range(値)
         
'''
