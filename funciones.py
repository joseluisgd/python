def prueba(rptaNo="Respondiste con un NO", rptaSi= "Respondiste con un SI"):
    while True:
        print ("Responder con un si o no")
        rpta= input()
        if rpta in ("s","si"):
            print(rptaSi)
            return True
        if rpta in ("n","no"):
            print(rptaNo)
            return False

#Insertando numeros en una lista
def f(a,L=None):
    if L is None:
        L=[]
    L.append(a)
    return L

def incrementador(n):
    return lambda x: x+n


if __name__ == "__main__":
    a=incrementador(1)
    print(a(0))
    a=incrementador(5)
    print(a(0))
