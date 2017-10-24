#Creación de conjuntos
A = set([1,2,3,4,5])
print("El conjunto A: {}".format(A))
B = set([4,5,6,7,8])
print("El conjunto B: {}".format(B))
#Unión
union = A.union(B)
print("La unión. A U B = {}".format(union))
#Intersección
interseccion = A.intersection(B)
print("La intersección. A ∩ B = {}".format(interseccion))
#Diferencia no es conmutativa
diferencia = A.difference(B)
print("La diferencia. A - B = {}".format(diferencia))
diferencia2 = B.difference(A)
print("La diferencia. B - A = {}".format(diferencia2))
#Diferencia simétrica
dif_simetrica = A.symmetric_difference(B)
print("La diferencia simétrica. A Δ B = {}".format(dif_simetrica))
