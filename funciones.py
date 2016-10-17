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


if __name__ == "__main__":
    prueba()
    print("\n")
    print("""\
    Personaliza el mensaje agregandole dos parametros en el mismo documento:
        Ejemplo:
        prueba('DIJE QUE NO!'','DIJE QUE SI!')
    """)
