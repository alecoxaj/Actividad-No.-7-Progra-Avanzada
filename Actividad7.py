def suma_lista(lista):
    return sum(lista)

def promedio_lista(lista):
    return sum(lista) / len(lista)

def positivos_negativos_ceros(lista):
    positivos = 0
    negativos = 0
    ceros = 0
    for num in lista:
        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1
        else:
            ceros += 1
    return positivos, negativos, ceros

def contar_multiplos_de_3(lista):
    multiplos = 0
    for num in lista:
        if num % 3 == 0:
            multiplos += 1
    return multiplos

def area_rectangulo(base, altura):
    return base * altura

def perimetro_rectangulo(base, altura):
    return 2 * base * altura

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def promedio_calificaciones(lista):
    suma = sum(lista)
    promedio = suma / len(lista)
    mayores = 0
    riesgo = 0
    for nota in lista:
        if nota >= 85:
            mayores += 1
        if nota < 60:
            riesgo += 1
    return promedio, mayores, riesgo

def mayor_lista(lista):
    return max(lista)

def menor_lista(lista):
    return min(lista)

def contar_repetidos(lista):
    contador = {}
    for num in lista:
        if num in contador:
            contador[num] += 1
        else:
            contador[num] = 1
    repetidos = 0
    for cantidad in contador.values():
        if cantidad > 1:
            repetidos += 1
    return repetidos

def calculadora(num1, num2, operacion):
    if operacion == '+':
        return num1 + num2
    elif operacion == '-':
        return num1 - num2
    elif operacion == '*':
        return num1 * num2
    elif operacion == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "No se puede dividir entre cero ¡Math Error!"
    else:
        return "Operación no válida"

while True:
    print("\nMenú")
    print("1. Análisis de lista de números reales")
    print("2. Área y perímetro del rectángulo")
    print("3. Verificar si un número es primo")
    print("4. Promedio de calificaciones y análisis")
    print("5. Análisis de lista de enteros")
    print("6. Calculadora básica")
    print("7. Salir")

    option = input("Selecciona una opción: ")

    match option:
        case "1":
            n = int(input("¿Cuántos números deseas ingresar? "))
            lista = []
            for i in range(n):
                num = float(input(f"Número {i+1}: "))
                lista.append(num)
            suma = suma_lista(lista)
            promedio = promedio_lista(lista)
            positivos, negativos, ceros = positivos_negativos_ceros(lista)
            multiplos = contar_multiplos_de_3(lista)
            print(f"La suma es: {suma}")
            print(f"El promedio es: {promedio}")
            print(f"Números positivos: {positivos}, Números negativos: {negativos}, Ceros: {ceros}")
            print(f"Multiplos de 3: {multiplos}")

        case "2":
            base = float(input("Ingresa la Base: "))
            altura = float(input("Ingresa la altura: "))
            area = area_rectangulo(base, altura)
            perimetro = perimetro_rectangulo(base, altura)
            print(f"El área es: {area}")
            print(f"El perímetro es: {perimetro}")

        case "3":
            num = int(input("Ingresa un número entero: "))
            if es_primo(num):
                print(f"{num} es primo")
            else:
                print(f"{num} no es primo")

        case "4":
            n = int(input("¿Cuántas calificaciones deseas ingresar? "))
            calificaciones = []
            for i in range(n):
                nota = float(input(f"Calificación {i+1}: "))
                calificaciones.append(nota)
            promedio, mayores, riesgo = promedio_calificaciones(calificaciones)
            print(f"El promedio es: {promedio}")
            print(f"Mayores o iguales a 85 es: {mayores}")
            print(f"En zona de riesgo (<60): {riesgo}")

        case "5":
            n = int(input("¿Cuántos números enteros deseas ingresar? "))
            lista = []
            for i in range(n):
                num = int(input(f"Número {i+1}: "))
                lista.append(num)
            mayor = mayor_lista(lista)
            menor = menor_lista(lista)
            repetidos = contar_repetidos(lista)
            print(f"Mayor: {mayor}")
            print(f"Menor: {menor}")
            print(f"Números Repetidos: {repetidos}")

        case "6":
            num1 = int(input("Ingresa el primer número: "))
            num2 = int(input("Ingresa el segundo número: "))
            operacion = input("Selcciona una operación: (+, -, *, /): ")
            resultado = calculadora(num1, num2, operacion)
            print(f"El resultado es: {resultado}")

        case "7":
            print("¡Programa finalizado!. Saliendo...")
            break

        case _:
            print("Opción inválida. ¡Inténtalo nuevamente!")

