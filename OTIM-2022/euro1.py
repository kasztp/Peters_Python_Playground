def bruh(pear):
    apple=["H","N","O","4","k","l","m","6","i","j","9","n","+","J","2","h","y","f","0","g","z","A","8","u","v","w","D","E","q","3","X","1","Q","7","Z","K","e","F","r","W","c","V","T","t","s","/","M","R","G","Y","b","d","x","S","o","=","I","L","a","U","p","P","B","C","5"];banana="";orange=""
    for seed in pear:
        if seed in apple: mango=bin(apple.index(seed)).lstrip("0b");mango=mango.zfill(6);banana+=mango
    grapes=[banana[x:x+8] for x in range(0,len(banana),8)]
    for grape in grapes:
        if int(grape,2)==0: continue
        orange += chr(int(grape,2))
    return orange


eval(bruh("5eZibAmDQq=EM/miLY8wblrvQekiC+WERYoEKF8EFJFicyWEVj6q"[::-1]))
