def longitud_union_intervalos(intervalos):
    intervalos.sort()  
    total = 0
    inicio, fin = intervalos[0]

    for li, ri in intervalos[1:]:
        if li <= fin:  
            fin = max(fin, ri)
        else:
            total += fin - inicio + 1
            inicio, fin = li, ri
    total += fin - inicio + 1  

    return total

n = 3
intervalos = [(1, 3), (2, 5), (7, 9)]
print(longitud_union_intervalos(intervalos))  