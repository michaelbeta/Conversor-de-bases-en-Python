#########################################################################
#
#	Conversor de bases numericas
#
#	Michael Betancourt Mora B81126
#
#########################################################################

## Funcion que convierte un numero binario a decimal
def binario_a_decimal(binario):

	decimal = 0
	n = 0
	for bit in binario[::-1]:

		decimal += int(bit) * 2**n
		n += 1

	return decimal


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

#########Complemento#####

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

###Fin de complemento#####

##Conforme a la base seleccioando realizara la conversion
def RealizarConversion(numero,base):

            if base==10:
                dec_to_bin=decimal_a_binario(numero)
                print("El numero "+ str(numero) +" en binario es : ",dec_to_bin)
                print("El complemento a 1 de "+ str(dec_to_bin) +" es: ", complemento_a_1(dec_to_bin))
                print("El complemento a 2 de "+ str(dec_to_bin) +" es: ", complemento_a_2(dec_to_bin)+"\n")
            elif base == 2:
                eleccion="Binario"
            elif base == 3:
                eleccion="Octal"
            elif base == 4:
                eleccion="Hexadecimal"

##Pregunta a que base corresponde el numero               
def TipodeBase_del_Numero(numero):
    
        opc=True
        while opc:
            selecciono=int(input("\nSeleccione el tipo de base del numero a ingresar\n"
                +"\n1)10"
                +"\n2)2"
                +"\n3)8"
                +"\n4)16\n"))
            if selecciono==1:
                RealizarConversion(numero,10)
                opc=False
            elif selecciono == 2:
                opc=False
            elif selecciono == 3:
                opc=False
            elif selecciono == 4:
                opc=False
            elif selecciono !="":
                print("\nValor no valido intentelo de nuevo\n")


#######################################
##                MAIN               ##
#######################################

opc=True
while opc:
     
        seleccion=int(input("Seleccione la conversion requerida\n"
            +"\n1)Decimal"
            +"\n2)Binaria"
            +"\n3)Octal"
            +"\n4)Hexadecimal"
            +"\n5)Salir\n")) 
        if seleccion==1:
            numero=int(input("Ingrese el numero: "))
            TipodeBase_del_Numero(numero)           
        elif seleccion==2:
            print("\n Binario") 
        elif seleccion==3:
            print("\n Octal") 
        elif seleccion==4:
            print("\n Hexadecimal")
        elif seleccion==5:
            opc=False
        elif seleccion !="":
            print("\nValor no valido intentelo de nuevo\n")

