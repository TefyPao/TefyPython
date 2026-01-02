##Calculadora
## Va a recibir dos números pero el usuario no puede escribir cualquier cosa
##usar la función 'input'
#debe tener suma, resta, división, multiplicación, división, potencia, módulo, entre dos números 

try: 
    print("Welcome to Tefy's calculator")
    print("A continuación, ingresa dos números y elige la operación del menú de opciones:")
    print("Menú de opciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potenciación")
    print("6. Módulo")
    x= float(input("Introduce el primer número:"))
    y= float(input("Introduce el 2do número:"))
    operation= input("¿Qué operación deseas hacer?: (Selecciona una opción del anterior menú de opciones)")
    

    if operation =="1":
        print("La suma de los dos números es:", x + y)
    elif operation=="2":
        print("El resultado de restar los dos números es:", x - y)
    elif operation== "3":
        print("El producto de los dos números es:", x ** y)
    elif operation== "4":
        print("El cociente de dividir los dos números es:", x / y)   
    elif operation== "5":
        print("La potencia es:", x ** y)    
    elif operation=="6":
        print("El módulo entre los dos números es:", x % y)
    else:
        print("Operación no válida.")

except ValueError:
    print("Hay un error. No se pueden operar números con letras")

except ZeroDivisionError: 
    print("División por cero no es posible")
except Exception as e: 
    print("¡Ha ocurrido un error!")



