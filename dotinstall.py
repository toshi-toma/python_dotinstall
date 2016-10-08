# coding: UTF-8

# -2- #
#　コメント

# -3- #
#　データ型
#　数値
#　真偽値 true false
#　None
#　関数・オブジェクト
#　要素が並んだもの
#　-文字列：文字が並んだもの
#　-リスト：データが並んだもの
#　-タプル：データが並んだもの(変更ができない)
#　-セット：データが並んだもの(重複を許さない)
#　-辞書：キーと値がペア
msg = "hello world"
print msg # コメント

# -4- #
#数値
#整数、小数、複素数
#演算子 + - / // % **
print 10 * 5
print 10 // 3
print 10 % 3
print 2 ** 3
#整数と小数の演算は小数
print 5 + 2.0
#整数同士の割り算は切り捨ての整数
print 10 / 3

# -5- #
#文字列
# "hello" 'hello'
#日本語　u"こんにちは"
# + *
#エスケープ ¥n ¥t ¥¥
print "hello + ""world"
print u"無駄" * 10
print 'hello\n wo \trld\\ it \'s a pen'
print """<html lang = "ja>
<body>
</body>
</html>"""

# -6- #
#文字列
#文字数
#検索　find
#切り出し　[] [start:end]
s = "abcdefghi"
print len(s)
print s.find("x")
print s[2:5]
print s[:5]
print s[2:]
print s[2:-1]

# -7- #
#数値 <> 文字列
#文字列 > 数値 int float
#数値 > 文字列 str
print 5 + int('5')
age = 20
print "i am" + str(age) + "years old"

# -8- #
#リスト
#len + * []
sales = [255, 100, 353, 400]
print len(sales)
print sales[2]
sales[2] = 100
print sales[2]
# in 存在チェック
print 100 in sales
#range
print range(10)
print range(3, 10, 2)

# -9- #
#リスト
sales = [50, 100, 80, 45]
# sort / reverse
sales.sort()
sales.reverse()
print sales
# 文字列とリスト
d = "2013/12/15"
print d.split("/")
a = ["a", "b", "c"]
print "-".join(a)

# -10- #
#タプル(変更ができない)
a = (2, 5, 8)
# len + * []
print len(a)
print a * 3
# タプル <> リスト
b = list(a)
print b
c = tuple(b)
print c

# -11- #
#セット(集合型) - 重複を許さない
a = set([1, 2, 3, 4])
b = set([3, 4, 5])
print a
# - 差集合
print a - b
# |　和集合
print a | b
# & 積集合
print a & b
# ^  どちらにも無い
print a ^ b

# -12- #
#辞書型　key value
sales = {"taguchi":200, "fkoji":300, "dotinstall":500}
print sales["taguchi"]
sales["fkoji"] = 800
print sales
# in
print "taguchi" in sales
# keys, values, items
print sales.keys()
print sales.values()
print sales.items()

# -13- #
a = 10
b = 1.234566
c = "taguchi"
d = {"fkoji":300, "dotinstall":500}
print "age: %d" %a
print "age: %10d" %a
print "age: %010d" %a
print "price: %f" %b
print "price: %.2f" %b
print "name: %s" %c
print "sales: %(fkoji)d" %d
print "%d and %f" %(a,b)

# -14- #
#条件分岐 if
#比較演算子 > < >= <= == !=
#論理演算子 and or not
score = 70
# if score > 60 and score < 80:
if 60 < score < 80:
    print "ok!"
    print "OK!"

# -15- #
#条件分岐 if
score = 45
if score > 60:
    print "ok"
elif score > 40:
    print "soso"
else:
    print "ng"
print "OK" if score > 60 else "NG"

# -16- #
#for ループ
sales = [13, 32, 21, 238]
sum = 0
for sale in sales:
    sum += sale
else:
    print sum
# continue break
for i in range(10):
    if i == 3:
        continue
    if i == 7:
        break
    print i



# -17- #
# -18- #
# -19- #
# -20- #
# -21- #
# -22- #
# -23- #
# -24- #