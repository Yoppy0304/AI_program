print("先攻、後攻選んでね！")
kuro = 0
shiro= 0

def tebanngime() :
    if input() == "先攻" :
            print("先攻になりました!")
            kuroihito = 0
    elif input() == "先攻" :
            print("後攻になりました!")
            siroihito = 1
    else:
         print("ちゃんと選ぼうね!!")


def hantei(kuro , shiro):
    if kuro > shiro:
        print("kuroの勝ち!!")

    elif kuro < shiro :
        print("shiroの勝ち!!")
    elif kuro == shiro :
        print("引き分け")
    else: 
        print("エラーが発生しました")

def tebanhyouji():
     print()

        




    
    
   