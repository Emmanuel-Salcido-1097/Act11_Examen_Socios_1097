# Se crea la clase
class socios1097:
    # Zona de atributos 
    ID_Socios=0
    Nombre=""
    Tipo_socio=""
    Contacto=0
    email=""
    Aporte=""
    Beneficio=""

    #Zona de funciones
    def Datos_socio(self,n,t_s,c,e,a,b):
        print(f"Nombre :{n}")
        print(f"Tipo de socio :{t_s}")
        print(f"Contacto :{c}")
        print(f"Email :{e}")
        print(f"Aporte :{a}")
        print(f"Beneficio :{b}")

    def Lista_socios():
        L_socios=["Carlos","David","Angel","Kristian","Emmanuel"]
        for x in L_socios:
            print(x)

    def Tupla_TipoS():
        T_socios=("Inversor","Laboral","Financiero","Transporte","Financiero")
        for y in T_socios:
            print(y)

    def Diccionario_email():
        D_socios={"Email 1":"carlos1212@gmail.com",
                    "Email 2":"davidmk532@gmail.com",
                    "Email 3":"angelmovi1234@gmail.com",
                    "Email 4":"elmen1010@gmail.com",
                    "Email 5":"emmanuel5280@gmail.com"}
        for a,b in D_socios.items():
            print(a,":",b)

    def Transferencia():
        print("La transferencia se realizo correctamente")

    def Deposito():
        print("El dinero fue depositado de forma segura")

# Zona de crear objeto
InfoSocios=socios1097

# añadir valores a los atributos
InfoSocios.ID_Socios=1
InfoSocios.Nombre="Carlos"
InfoSocios.Tipo_socio="Inversor"
InfoSocios.Contacto="656-922-2720"
InfoSocios.email="carlos1212@gmail.com"
InfoSocios.Aporte="Monetario"
InfoSocios.Beneficio="Conexiones(mutuo)"

# Zona de mostrar funciones
print("\n----------Datos del socio----------")
InfoSocios.Datos_socio(InfoSocios.ID_Socios,InfoSocios.Nombre,InfoSocios.Tipo_socio,
                        InfoSocios.Contacto,InfoSocios.email,InfoSocios.Aporte,InfoSocios.Beneficio)
print("\n-----Socios----------------\n")
InfoSocios.Lista_socios()
print("\n-----Tipo de socio---------\n")
InfoSocios.Tupla_TipoS()
print("\n-----Emails de los socios--\n")
InfoSocios.Diccionario_email()
print("\nResultado de transferencia-")
InfoSocios.Transferencia()
print("\n----Resultado de deposito--")
InfoSocios.Deposito()