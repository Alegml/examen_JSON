import json

base_de_datos = {}

while True:
    print("¿Qué acción quieres realizar?")
    print("1. Agregar alumnos")
    print("2. Listar alumnos")
    print("3. Calcular Promedio de las notas de la clase")
    print("4. Nota Maxima y minima")
    print("5. Guardar Datos")
    print("6. Salir")
    opcion = int(input("Opción: "))
    
    if opcion == 1:
        nombre = input("Nombre del Alumno: ")
        edad = int(input("Edad del alumno: "))
        notas=[]
        nota=""
        seguir=True
        while seguir:
            if nota != -1:
                nota = float(input("Notas de las materias (Para terminar coloque -1): "))
                notas.append(nota)
            else:
                seguir=False
                notas.remove(-1)

        base_de_datos[nombre] = {'Edad':edad , 'Notas': notas}
    
    elif opcion == 2:
        for clave, valor in base_de_datos.items(): 
            print ("El alumno: %s Tiene Las siguientes notas: %s" % (clave, valor.get('Notas')))
            print("")
        
    elif opcion == 3:
        promedio_clase=0
        contador=0
        for clave, valor in base_de_datos.items():
            promedio=0
            for nota in valor.get('Notas'):
                promedio+=nota
            promedio= promedio/len(valor.get('Notas'))
            promedio_clase+= promedio
            contador+=1
            print(f"El promedio de {clave} es de: {promedio}")
        promedio_clase= promedio_clase/contador
        print (f"El promedio de la Clase es: {promedio_clase}")

    elif opcion == 4:
        nota_menor=20
        nota_mayor=20
        alumno_nota_mayor=""
        alumno_nota_menor=""
        
        for clave, valor in base_de_datos.items():
            for nota in valor.get("Notas"):
                if nota<nota_menor:
                    nota_menor=nota
                    alumno_nota_menor= clave
                
                if nota>=nota_mayor:
                    nota_mayor=nota
                    alumno_nota_mayor= clave

        print(f"El alumno con la Mayor Nota fue: {alumno_nota_mayor} con una nota de: {nota_mayor}")
        print(f"El alumno con la Menor Nota fue: {alumno_nota_menor} con una nota de: {nota_menor}")

    elif opcion == 5:
        with open ("base_de_datos.json", 'w') as file:
            json.dump(base_de_datos, file, indent=2)
        print("Sus datos se han guardado correctamente")

    elif opcion == 6:
        break

    else:
        print("Opción inválida. Inténtalo de nuevo.")

'''with open('datos.json', 'w') as file:
    json.dump(base_de_datos,file)'''


