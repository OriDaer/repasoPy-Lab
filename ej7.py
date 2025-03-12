name=str(input('ingresa tu nombre: '))
edad=int(input('ingresa tu edad: '))
city=str(input('ingresa tu ciudad de residencia: '))
añoNacim=2025-edad
print(f'Hola {name} eres de {city} y naciste en {añoNacim}')
if(edad>=18):
    print('eres mayor de edad')
else:
    print('eres menor de edad')
if(edad%5):
    print('tu edad es multiplo de 5')
else:
    print('tu edad no es multiplo de 5')
