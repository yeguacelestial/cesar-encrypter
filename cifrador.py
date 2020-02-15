# a. Impresion en terminal del contenido de un archivo
# b. Cifrado César con desfase de tres posiciones para un texto
# c. Cifrado César con desfase de x posiciones para un texto
# d. Generación de cuatro primeros caractéres para RFC o CURP
# e. Impresión en pantalla del contenido de un cifrador (diccionario)

import sys

def main():
	try:
		# Inciso a
		archivo = sys.argv[1]
		nom = nombre(archivo)

		# Inciso b
		cesar3 = generar_cifrador(3)
		nom_cifrado = cifrar(nom, cesar3)
		mostrar_cifrado(nom_cifrado, 3)

		# Inciso c
		offset = int(sys.argv[2])
		cifrado_x = generar_cifrador(offset)
		nom_cifrado = cifrar(nom, cifrado_x)
		mostrar_cifrado(nom_cifrado, offset)

		# Inciso d
		curp(nom)

		# Inciso e
		mostrar_cifrador(offset)

	# Excepción para cuando se manda un offset inválido
	except ValueError as e:
		print("[-] Error: El argumento del offset es inválido.")

	# Excepción general
	except Exception as e:
		print("[*] Uso: cifrador.py <archivo-ascii> <valor-offset>")

def nombre(archivo):
	try:
		with open(f'{archivo}', 'r') as f:
			nombre = f.read()
			print(f'[+] Tu nombre es: {nombre}')
		return nombre
	except Exception as e:
		print("[-] Error: el archivo no existe o está corrupto.")

def generar_cifrador(offset):
	try:
		letras=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		letras_cifradas=[]

		posicion = 0
		tope = len(letras)

		for i in range(tope):
			if (i+offset < tope):
				posicion = i + offset
				letras_cifradas.append(letras[posicion])
			else:
				posicion = abs((tope-i) - offset)
				letras_cifradas.append(letras[posicion])

		cesarx = dict(zip(letras, letras_cifradas))
		return cesarx

	except Exception as e:
		print(f"[-] Error: {e}")

def cifrar(palabra,cifrador):
	nombre_cifrado = []

	for c in list(palabra):
		if c == ' ':
			nombre_cifrado.append(c)

		for k, v in cifrador.items():
			if k == c:
				nombre_cifrado.append(v)
			else:
				pass
	
	nombre_cifrado = "".join(nombre_cifrado)
	return nombre_cifrado

def mostrar_cifrado(palabra, offset):
	print(f"[+] Tu nombre cifrado con cesar{offset} es: {palabra}")

def curp(nombre):
	nombre = nombre.split()
	longitud = len(nombre)
	vocales = ['a', 'e', 'i', 'o', 'u']
	iniciales_curp = []

	if (longitud >= 3):
		apellido_paterno = nombre[-2]
		apellido_materno = nombre[-1]
		nombre_pila = nombre[0]

		primera_letra_pa = apellido_paterno[0]
		primera_vocal_pa = ""
		primera_letra_sa = apellido_materno[0]
		primera_letra_np = nombre_pila[0]

		for letra in apellido_paterno[::-1]:
			for vocal in vocales:
				if letra == vocal:
					primera_vocal_pa = letra

		iniciales_curp.append(primera_letra_pa)
		iniciales_curp.append(primera_vocal_pa)
		iniciales_curp.append(primera_letra_sa)
		iniciales_curp.append(primera_letra_np)
		iniciales_curp = "".join(iniciales_curp)

		iniciales_curp = iniciales_curp.upper()

		iniciales_curp = f"[+] Código para CURP o RFC: {iniciales_curp}"
		return print(iniciales_curp)
	
	else:
		print("[*] Debe ser el nombre completo. (Minimo: un nombre y dos apellidos)")

def mostrar_cifrador(offset):
	cifrador = generar_cifrador(offset)

	for k, v in cifrador.items():
	 	print(f"[*] Letra: {k} - Letra cifrada: {v}")

if __name__ == '__main__':
	main()
