def longitud_subcadena_sin_repetidos(s):
    ultima_pos = {}
    izquierda = 0
    max_long = 0

    for derecha, char in enumerate(s):
        if char in ultima_pos and ultima_pos[char] >= izquierda:
            izquierda = ultima_pos[char] + 1
        ultima_pos[char] = derecha
        max_long = max(max_long, derecha - izquierda + 1)

    return max_long


s = "abcabcbb"
print(longitud_subcadena_sin_repetidos(s)) 