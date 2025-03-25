def validMountainArray(arr: list[int]) -> bool:
    # Retorna False se o array for menor que 3 itens
    if len(arr) < 3:
        return False
    
    # Encontra o maior valor (pico)
    p = 0
    while p < len(arr) - 1 and arr[p] < arr[p + 1]:
        p += 1
    
    # Verifica se o pico não está no começo nem no fim
    if p == 0 or p == len(arr)- 1:
        return False
    
    # Verifica se elementos depois do pico estão em ordem decrescente
    while p < len(arr) - 1:
        if arr[p] <= arr[p + 1]:
            return False
        p += 1
    
    return True


example1 = [2,1] # **Output:** false
example2 = [3,5,5] # **Output:** false
example3 = [0,3,2,1] # **Output:** true

print(f'RESULT: {validMountainArray(example1)}; EXPECTED OUTPUT: False')
print(f'RESULT: {validMountainArray(example2)}; EXPECTED OUTPUT: False')
print(f'RESULT: {validMountainArray(example3)}; EXPECTED OUTPUT: True')
