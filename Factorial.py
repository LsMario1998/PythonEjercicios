"""def Ex(*name):
    print("nombre: ", name)
Ex('Mario','Labbé','Sanhueza')"""
"""def name2(a,n):
    print(n, a)
name2(a='labbe', n='mario')
"""
"""def nam3(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])

nam3(nombre='mario', apellido='labbe')"""

def Recursion(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n*Recursion(n-1)

aa=Recursion(12)
print(aa)

