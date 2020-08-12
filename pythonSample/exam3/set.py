# set/辞書

st = {'hi', 'hello', 'ok'}
st.add('welcome')
st.remove('ok')
print(st)


st1 = {10, 20, 30}
st2 = {10, 2, 30}
var1 = st1 & st2
var2 = st1 | st2
var3 = st1 ^ st2
var4 = st1 - st2
print(var1)
print(var2)
print(var3)
print(var4)

dc = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
dc['e'] = 1000
dc['a'] = dc['b'] + dc['c']
print(dc)


dc1 = {'a': 100, 'b': 200, 'c': 300}
var5 = list(dc1.keys())
var6 = list(dc1.values())
var7 = list(dc1.items())
print(var5)
print(var6)
print(var7)


'''

 # セットの作成
 　　　　{値1, 値2,....}
 
 # set関数によるセットの作成
       set{シーケンス値}
       
 # 値があるか調べる
 　　　　値　in セット
 　　　　値　not in セット
 
 # 値を追加する
       セット.add(値)
       
 # 値を取り除く
 　　　　セット.remove(値)
 
 # 辞書の作成
 　　{キー: 値1, キー: 値2,....}
     dict(キー1 = 値1 ,キー2 = 値2,...)
     
 # 値を取り出す
     辞書[キー]
     
　# 値を変更する
　　　辞書[キー]　= 値

 # 辞書の値の削除
     del 辞書[キー]
     
 # 全てのキーワードを得る
     辞書.keys()
     
 # 全ての値を得る
 　　辞書.values()
 
 # 全ての項目を得る
    辞書.items()
    
'''