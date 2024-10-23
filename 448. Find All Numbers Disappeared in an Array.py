def findDisappearedNumbers(nums: list[int]) -> list[int]:
    n = len(nums)  # Calcula o tamanho da lista
    result = []  # Inicializa uma lista para armazenar os números que faltam

    # Utilize a lista original como um "hash table" e varre a lista convertende em negativo os numeros encontrados
    for i in range(n):  # Itera sobre cada elemento da lista
        index = abs(nums[i]) - 1  # Calcula qual seria o índice correspondente ao número atual caso fosse uma lista ordenada
        if nums[index] > 0:  # Se o número no índice for positivo, significa que o índice ainda não foi encontrado
            nums[index] *= -1  # Transforma o número em negativo, marcando o índice como encontrado

    # Itere sobre a lista para encontrar números positivos (índices que faltam)
    for i in range(n):  # Itera sobre cada elemento da lista
        if nums[i] > 0:  # Se o número for positivo, significa que o índice não foi encontrado na iteração anterior
            result.append(i + 1)  # Adiciona o índice + 1 (o número que falta) à lista de resultados

    return result


"""UNIT TESTS"""
import unittest

class TestfindDisappearedNumbers(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]), [5, 6])
        
    def test_2(self):
        self.assertEqual(findDisappearedNumbers([1, 1]), [2])


if __name__ == '__main__':
    unittest.main()
