#########################################################################
#
#	Conversor de bases numericas
#       Autores:
#	Michael Betancourt Mora B81126
#       Fernando Sánchez Moraga B97268
#       Michael Rodriguez Quesada B96713
#
#
#
#########################################################################

##Funciones obtenidas gracias  parzibyte (https://parzibyte.me/blog/2020/12/15/conversor-numeros-python/)
def obtener_caracter_hexadecimal(valor):
    # Lo necesitamos como cadena
    valor = str(valor)
    equivalencias = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor


def decimal_a_hexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:
        residuo = decimal % 16
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal / 16)
    return hexadecimal


def obtener_valor_real(caracter_hexadecimal):
    equivalencias = {
        "f": 15,
        "e": 14,
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10,
    }
    if caracter_hexadecimal in equivalencias:
        return equivalencias[caracter_hexadecimal]
    else:
        return int(caracter_hexadecimal)


def hexadecimal_a_decimal(hexadecimal):
    # Convertir a minúsculas para hacer las cosas más simples
    hexadecimal = hexadecimal.lower()
    # La debemos recorrer del final al principio, así que la invertimos
    hexadecimal = hexadecimal[::-1]
    decimal = 0
    posicion = 0
    for digito in hexadecimal:
        # Necesitamos que nos dé un 10 para la A, un 9 para el 9, un 11 para la B, etcétera
        valor = obtener_valor_real(digito)
        elevado = 16 ** posicion
        equivalencia = elevado * valor
        decimal += equivalencia
        posicion += 1
    return decimal
#-----------------------------------------------------------------------------------------------#
###Fin de funciones de parzibyte

## Metodo que convierte un numero binario a decimal
def binario_a_decimal(binario):
    posicion = 0
    decimal = 0
    binario = binario[::-1]
    for digito in binario:
        # Elevar 2 a la posición actual
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    return decimal
#Fin del método de binario a decimal#
#-----------------------------------------------------------------------------------------------#
#Método de conversión de decimal a octal#
def decimal_a_octal(decimal):
    octal=""
    while decimal > 0:
        residuo = decimal % 8
        octal = str(residuo) + octal
        decimal = int(decimal/8)
    return octal
#Fin del método de decimal a octal#
#-----------------------------------------------------------------------------------------------#
#Método de conversión de octal a decimal#
def octal_a_decimal(octal):
    decimal=0
    posicion=0

    octal = octal[::-1]
    for digito in octal:
        valor_entero = int(digito)
        numero_elevado = int(8 ** posicion)
        equivalencia = int(numero_elevado * valor_entero)
        decimal+= equivalencia
        posicion+=1
    return decimal
#Fin del método de conversión de octal a decimal#
#-----------------------------------------------------------------------------------------------#
## Funcion que convierte un numero decimal a binario 
def decimal_a_binario(decimal, n=None):

	if n == None:
		binario = []
		i = 0
		while decimal > 0:
			residuo = decimal % 2#Almacena el residuo
			binario.append(residuo)
			decimal = decimal // 2##Se obtiene la division sin decimal
			i += 1

	else:
		binario = [0] * n
		i = 0
		while decimal > 0:
			residuo = decimal % 2
			binario[i] = residuo
			decimal = decimal // 2
			i += 1

	binario.reverse()
	

	return ''.join([str(bit) for bit in binario])
#Fin de la función de conversión de decimal a binario#
#-----------------------------------------------------------------------------------------------#
#Parte de los complementos #
def complemento_base(numero, base_del_numero):

        base= str(base_del_numero)
        
        #complemento en base en hexadecimal
        if base == "16":
            total_valormaximo=""
            
            numero_n_de_digitos =len(numero)
            while numero_n_de_digitos>len(total_valormaximo):

                total_valormaximo+="F"


            numero_en_complemento_de_base=hexadecimal_a_decimal(total_valormaximo)-hexadecimal_a_decimal(numero)
            resultado=0

            if(numero_en_complemento_de_base!=0):
                resultado=decimal_a_hexadecimal(numero_en_complemento_de_base)

            return resultado

       #complemento en base en octal 
        elif base == "8":
            total_valormaximo=""
            
            numero_n_de_digitos = len(numero)
            while numero_n_de_digitos>len(total_valormaximo):

                total_valormaximo+="7"


            numero_en_complemento_de_base=int(total_valormaximo)-int(numero)
            resultado=0

            if(numero_en_complemento_de_base!=0):
                resultado=numero_en_complemento_de_base
            
            return resultado

        #complemento en base en decimal
        elif base == "10":

            total_valormaximo=""
            numero_n_de_digitos = len(numero)
            while numero_n_de_digitos>len(total_valormaximo):

                total_valormaximo+="9"


            numero_en_complemento_de_base=int(total_valormaximo)-int(numero)
            resultado=0

            if(numero_en_complemento_de_base!=0):
                resultado=numero_en_complemento_de_base
            
            return resultado

        #complemento en base a1 y a2 en binario
        elif base == "2":
           numero_en_complemento_de_base = complemento_a_1(str(numero))
           numero_en_complemento_de_base2 = complemento_a_2(str(numero))
           return numero_en_complemento_de_base2


## fin de funcion de complemento
## Funcion que obtiene el complemento a 1 de numero
def complemento_a_1(binario):

    n = len(binario)
    complemento = (2**n - 1) - binario_a_decimal(binario)

    return decimal_a_binario(complemento, n)

## Funcion que obtiene el complemento a 2 de numero
def complemento_a_2(binario):

    n = len(binario)
    complemento = 2**n - binario_a_decimal(binario)

    return decimal_a_binario(complemento, n)	
#-----------------------------------------------------------------------------------------------#
#Conversión a hexadecimal#
def Conversion_a_hexa(numero,base):
    if base==10:
        hexa=decimal_a_hexadecimal(int(numero))
        complemento=complemento_base(numero, base)
        print("El numero "+str(numero)+" en hexa es: ",hexa)
        print("El complemento de base de "+ str(numero)+" (10)" +" es: "+str(complemento)+"\n")
    if base==8:
        decimal=octal_a_decimal(numero)
        Hexadecimal=decimal_a_hexadecimal(decimal)
        complemento=complemento_base(numero, base)
        print("El numero "+str(numero)+" en hexa es: ",Hexadecimal)
        print("El complemento de base de "+ str(numero)+" (8)" +" es: "+str(complemento)+"\n")
    if base==2:
        decimal=binario_a_decimal(numero)
        Hexadecimal=decimal_a_hexadecimal(decimal)
        complemento=complemento_base(numero, base)
        print("El numero "+str(numero)+" en hexa es: ",Hexadecimal)
        print("El complemento de base de "+ str(numero)+" (2)" +" es: "+str(complemento)+"\n")
    

#Fin del método de conversión#
#-----------------------------------------------------------------------------------------------#
##Conforme a la base seleccioando realizara la conversion a binario
def Conversion_a_binario(numero,base):

            if base==10:
                Binario=decimal_a_binario(int(numero))
                complemento=complemento_base(numero, base)
                print("El numero "+ str(numero) +" en binario es : ",Binario)
                print("El complemento de base de "+ str(numero)+" (10)" +" es: "+str(complemento)+"\n")
            if base == 8:
                decimal=octal_a_decimal(numero)
                Binario=decimal_a_binario(int(decimal))
                complemento=complemento_base(numero, base)
                print("El numero "+ str(numero) +" en binario es : ",Binario)
                print("El complemento de base de "+ str(numero)+" (8)" +" es: "+str(complemento)+"\n")
            if base == 16:
                Decimal=hexadecimal_a_decimal(numero)
                Binario=decimal_a_binario(int(Decimal))
                complemento=complemento_base(numero, base)
                print("El numero "+ str(numero) +" en binario es : ",Binario)
                print("El complemento de base de "+ str(numero)+" (16)" +" es: "+str(complemento)+"\n")
                
#Fin del método de conversión a binario#
#-----------------------------------------------------------------------------------------------#
def Convertir_complemento1_BaseIndicada(complemento1):

    convertir=""
    for i in complemento1:
            convertir+=i

            
    return convertir

def Convertir_complemento2_BaseIndicada(complemento2):

    convertir=""
    for i in complemento2:
            convertir+=i

            
    return convertir

            
#Metodo para hacer la convercion a decimal 
def Conversion_a_decimal(numero,base):

    if base==2:
        decimal=binario_a_decimal(numero)
        complemento=complemento_base(numero, base)
        print("El numero "+str(numero)+" base(2) en base 10 es: ",decimal)
        print("El complemento de base de "+ str(numero)+" (2)" +" es: "+str(complemento)+"\n")
    if base==8:
        decimal=octal_a_decimal(numero)
        complemento=complemento_base(numero, base)
        print("El numero "+str(numero)+" base(8) en base 10 es: ",decimal)
        print("El complemento de base de "+ str(numero)+" (8)" +" es: "+str(complemento)+"\n")
    if base==16:
        Decimal=hexadecimal_a_decimal(numero)
        complemento=complemento_base(numero, base)
        print("El numero "+str(numero)+" base(16) en base 10 es: ",Decimal)
        print("El complemento de base de "+ str(numero)+" (16)" +" es: "+str(complemento)+"\n")
#Fin del método#
#-----------------------------------------------------------------------------------------------#
#Metodo para hacer la convercion a octal
def Conversion_a_octal(numero,base):
    if base==10:
        octal=decimal_a_octal(int(numero))
        complemento=complemento_base(numero, base)
        print("El numero "+str(numero)+"(10) en base 8 es: ",octal)
        print("El complemento de base de "+ str(numero)+" (10)" +" es: "+str(complemento)+"\n")
    if base==2:#recibe un numero binario
        decimal=binario_a_decimal(numero)
        octal=decimal_a_octal(decimal)
        complemento=complemento_base(numero, base)
        print("El numero "+str(numero)+"(2) en base 8 es: ",octal)
        print("El complemento de base de "+ str(numero)+" (2)" +" es: "+str(complemento)+"\n")
    if base==16:#Recibe un hexadecimal
        Decimal=hexadecimal_a_decimal(numero)
        octal=decimal_a_octal(Decimal)
        complemento=complemento_base(numero, base)
        print("El numero "+str(numero)+"(16) en base 8 es: ",octal)
        print("El complemento de base de "+ str(numero)+" (16)" +" es: "+str(complemento)+"\n")

#-----------------------------------------------------------------------------------------------#
##Metodo en el que se escoje a que base se va a realizar la conversion
def Elegir_conversion(numero,base):
#Inicio del bucle del menú secundario de elección de conversión#
        opc=True
        while opc:
            selecciono=int(input("\nA que base desea convertir el numero "+str(numero)+"\n"
                +"\n1)Decimal(10)"
                +"\n2)Binario(2)"
                +"\n3)Octal(8)"
                +"\n4)Hexadecimal(16)"))
            #Selección de la conversión a base Decimal#
            if (selecciono==1) and (base != 10):
                Conversion_a_decimal(numero,base)
                opc=False
            #Selección de la conversión a base Binario#
            if (selecciono == 2)and (base != 2):
                Conversion_a_binario(numero,base)
                opc=False
            #Selección de la conversión a base octal#
            if (selecciono == 3) and (base != 8):
                Conversion_a_octal(numero,base)
                opc=False
            #Selección de la conversión a base Hexadecimal#
            if (selecciono == 4) and (base != 16):
                Conversion_a_hexa(numero,base)
                opc=False
            if selecciono > 4:
                print("\nValor no valido intentelo de nuevo\n")
#Fin del menú secundario de selección#
#-----------------------------------------------------------------------------------------------#  
#######################################
##                MAIN               ##
#######################################
                
#Inicio del bucle para el menú principal#
opc=True
while opc:

        print("****************************************************************") 
        seleccion=int(input("Seleccione la base del numero que va a ingresar\n"
            +"\n1)Decimal(10)"
            +"\n2)Binario(2)"
            +"\n3)Octal(8)"
            +"\n4)Hexadecimal(16)"
            +"\n5)Salir\n"))
        #Acción de la consola si se selecciona el numero 1(Decimal)#
        if seleccion==1:
            numero=input("Ingrese el numero: ")
            base=10
            Elegir_conversion(numero, base)
        #Acción de la consola si se selecciona el numero 2(Binario)# 
        elif seleccion==2:
            base=2
            numero=input("Ingrese el numero: ")
            Elegir_conversion(numero, base)
        #Acción de la consola si se selecciona el numero 3(Octal)#    
        elif seleccion==3:
            base=8
            numero=input("Ingrese el numero: ")
            Elegir_conversion(numero, base)
        #Acción de la consola si se selecciona el numero 4(Hexadecimal)#
        elif seleccion==4:
            base=16
            numero=input("Ingrese el numero: ")
            Elegir_conversion(numero, base)
        #Acción de la consola si se selecciona el numero 5(Salir)#
        elif seleccion==5:
            print("Hasta pronto !")
            opc=False
        #Exepción si se ingresa un número indebido# 
        elif seleccion>5 or seleccion<0:
            print("\nValor no valido intentelo de nuevo\n")
#Fin del menú#
#-----------------------------------------------------------------------------------------------#

