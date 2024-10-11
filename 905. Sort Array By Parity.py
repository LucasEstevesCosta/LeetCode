def sortArrayByParity(nums: list[int]) -> list[int]:
    if len(nums) <= 0:
        return nums
    pi = 0  # PonteiroInicial começa em 0
    pf = len(nums) - 1  # Ponteiro final começa em -1

    while pi < pf:  # Itera sobre a lista enquanto PonteiroInicial for menor que PonteiroFinal.
        # Se PonteiroInicial for impar e PonteiroFinal par, trocam de posição e avançam uma casa.
        if nums[pi] % 2 != 0 and nums[pf] % 2 == 0:
            nums[pi], nums[pf] = nums[pf], nums[pi]
            pi += 1
            pf -= 1

        # Se quer dizer que ou o PonteiroInicial é par ou o PonteiroFinal é impar
        else:
            if nums[pi] % 2 == 0: # Se o PonteiroInicial for par
                pi += 1 # Aí o PonteiroInicial anda e o PonteiroFinal não.

            else: # Se não quer dizer que o PonteiroInicial é impar e o PonteiroFinal é impar.
                pf -= 1 # Nesse caso o PonteiroFinal anda.

    return nums


"""Test Cases"""
example1 = [3, 1, 2, 4]  # Output:  [2, 4, 3, 1]
example2 = [0]  # Output: [0]
example3 = [0, 1]
sortArrayByParity(example1)
sortArrayByParity(example2)
sortArrayByParity(example3)
print(f'RESULT: {example1}; EXPECTED OUTPUT: [P, P, I, I]')
print(f'RESULT: {example2}; EXPECTED OUTPUT: [0]')
print(f'RESULT: {example3}; EXPECTED OUTPUT:')
