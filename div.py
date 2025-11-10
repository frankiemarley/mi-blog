def encontrar_max_min_dc(arr, inicio, fin):
    """
    Encuentra el máximo y mínimo en un array usando divide y conquista
    """
    # Caso base: un elemento
    if inicio == fin:
        return arr[inicio], arr[inicio]
    
    # Caso base: dos elementos
    if fin == inicio + 1:
        if arr[inicio] < arr[fin]:
            return arr[inicio], arr[fin]
        else:
            return arr[fin], arr[inicio]
    
    # Divide: encontrar punto medio
    medio = (inicio + fin) // 2
    
    # Conquista: resolver subproblemas
    min_izq, max_izq = encontrar_max_min_dc(arr, inicio, medio)
    min_der, max_der = encontrar_max_min_dc(arr, medio + 1, fin)
    
    # Combina: unir soluciones
    min_total = min(min_izq, min_der)
    max_total = max(max_izq, max_der)
    
    return min_total, max_total

def encontrar_max_min_iterativo(arr):
    """
    Versión iterativa para comparación
    """
    if not arr:
        return None, None
    
    min_val = max_val = arr[0]
    
    for num in arr[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    
    return min_val, max_val

# Función principal para pruebas
def main():
    # Pruebas con diferentes casos
    test_cases = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1],
        [2, 1],
        [3, 1, 4, 1, 5, 9, 2, 6],
        [-1, -2, -3, -4],
        [10]
    ]
    
    print("=== PRUEBAS ALGORITMO DIVIDE Y CONQUISTA ===\n")
    
    for i, arr in enumerate(test_cases):
        print(f"Test case {i+1}: {arr}")
        
        # Algoritmo divide y conquista
        if len(arr) > 0:
            min_dc, max_dc = encontrar_max_min_dc(arr, 0, len(arr)-1)
            min_it, max_it = encontrar_max_min_iterativo(arr)
            
            print(f"Divide y conquista: Mínimo = {min_dc}, Máximo = {max_dc}")
            print(f"Algoritmo iterativo: Mínimo = {min_it}, Máximo = {max_it}")
            
            # Verificar que dan el mismo resultado
            if min_dc == min_it and max_dc == max_it:
                print("✓ Resultados coinciden")
            else:
                print("✗ ERROR: Resultados no coinciden")
        else:
            print("Array vacío")
        
        print("-" * 50)

# Análisis de complejidad
def analizar_complejidad():
    """
    Demuestra la complejidad del algoritmo
    """
    print("\n=== ANÁLISIS DE COMPLEJIDAD ===")
    print("Algoritmo Divide y Conquista:")
    print("T(n) = 2T(n/2) + O(1)")
    print("Por el teorema maestro: O(n)")
    print("\nComparación con algoritmo iterativo:")
    print("Ambos son O(n), pero divide y conquista tiene")
    print("mejor paralelización potencial")

if __name__ == "__main__":
    main()
    analizar_complejidad()