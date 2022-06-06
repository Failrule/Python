def Decodificar(elemento):
    for i, val in enumerate(elemento):
        for j, vul in enumerate(val):
            item=0
            while item < vul[0]:
                print(vul[1],end="")
                item=item+1
        print("\n")