# Варіант 5, m (розмірність поля) = 233, p(x) (генератор поля) = x**233 + x**9 + x**4 + x + 1 
import time


m = 233
p = '100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000010011'

def toTheSameLength(A, B):
    if len(A) < len(B):
        A = [0] * (len(B) - len(A)) + A
    if len(A) > len(B):
        B = [0] * (len(A) - len(B)) + B
    return A, B  

def deleteExtraZeros(A):
    while A and A[0] == 0:
        A.pop(0)
    if not A:
        return [0]
    return A

def stringToArray(n):
    result = result = list(map(int, n))
    result = deleteExtraZeros(result)
    return result

def arrayToString(n):
    while len(n) > m:
        n.pop(0)
    n = list(map(str, n))
    while len(n) < m:
        n = ['0'] + n
    result = ''.join(n)    
    return result

def fieldGalueModule(A, N):
    A = deleteExtraZeros(A)
    if len(A) < len(N):
        return A
    for i in range(len(N)):
        A[i] = (A[i] + N[i]) % 2
    A = deleteExtraZeros(A)
    return fieldGalueModule(A, N)

def fieldGalueAdd(A, B):
    A = deleteExtraZeros(A)
    B = deleteExtraZeros(B)
    A, B = toTheSameLength(A, B)
    result = []
    for i in range(len(A)):
        k = int(A[i]) + int(B[i])
        n = k % 2
        result.append(n)
    result = deleteExtraZeros(result)    
    return result

def fieldGalueMul(A, B, N):
    A = deleteExtraZeros(A)
    B = deleteExtraZeros(B)
    A, B = toTheSameLength(A, B)
    k = len(A)
    t = len(B)
    result = [0] * (k * 2 - 1)
    for i in range(k):
        if A[i] == 1:
            for j in range(len(B)):
                result[i + j] = (result[i + j] + B[j]) % 2
    result = fieldGalueModule(result, N)            
    return deleteExtraZeros(result)

def fieldGalueSquarePower(A, N):
    result = fieldGalueMul(A, A, N)
    return result

def fieldGaluePower(A, B, N):
    B = B[::-1]
    result = [1]
    for i in B:
        if i == 1:
            result = fieldGalueMul(result, A, N)
        A = fieldGalueSquarePower(A, N)
    return result

def fieldGalueTrace(A, N):
    A = deleteExtraZeros(A)
    k = A
    result = A
    for _ in range(1, m):
        k = fieldGalueSquarePower(k, N)
        result = fieldGalueAdd(result, k)
    result = sum(result) % 2
    result = stringToArray(str(result))
    return result

def fieldGalueInverseElement(A, N):
    k = bin(2**m - 2)[2:]
    k = stringToArray(k)
    result = fieldGaluePower(A, k, N)
    return result

def fieldGaluefindZero(A):
    result = fieldGalueAdd(A, A)
    return result

def fieldGaluefindOne(A, N):
    A = deleteExtraZeros(A)
    if A == [0]:
         raise Exception('Error')
    A1 = fieldGalueInverseElement(A, N)
    result = fieldGalueMul(A, A1, N)
    return result

f = '11011011110110001011101001001010100110010000100110101101101011101110101010011110001110011010011101010111111010001010111101101101110110001100011010010011111111001111000001011101010001110110111100110101011100101110101010011100010101011'
g = '10101101110111111101111110100011001100100111110110010010101111111110111000010011111111101110010110010111000010110010001101001010101001011011110101000110001001110101111101010100100101011010000011101010011011000001011010111001000010001'
#h = '10101001011010010000000001001101111100001111001101000010100010000001011000101110100000000000000000011111001111000100000110010111110001110101000011111111011101101001101101111010000001101100000110001111110011101010110011010111000100010'
pp = stringToArray(p)
ff = stringToArray(f)
gg = stringToArray(g)
#hh = stringToArray(h)

print()
print('fieldGaluefindZero: ' + arrayToString(fieldGaluefindZero(ff)))
print()
print('fieldGaluefindOne: ' + arrayToString(fieldGaluefindOne(ff, pp)))
print()
print('fieldGalueAdd: ' + arrayToString(fieldGalueAdd(gg, ff)))
print()
print('fieldGalueMul: ' + arrayToString(fieldGalueMul(gg, ff, pp)))
print()
print('fieldGalueTrace: ' + arrayToString(fieldGalueTrace(ff, pp)))
print()
print('fieldGalueSquarePower: ' + arrayToString(fieldGalueSquarePower(ff, pp)))
print()
print('fieldGaluePower: ' + arrayToString(fieldGaluePower(ff, gg, pp)))
print()
print('fieldGalueInverseElement: ' + arrayToString(fieldGalueInverseElement(ff, pp)))

'''print(arrayToString(ff))
print(fieldGalueAdd(ff, gg))
print(fieldGalueModule(ff, pp))
print(fieldGalueMul(ff, gg, pp))
print(fieldGaluePower(gg, hh, pp))
print(fieldGalueInverseElement(gg, pp))
print(fieldGaluefindOne(ff, pp))
print(fieldGaluefindZero(ff))
print(fieldGalueMul(fieldGalueInverseElement(gg, pp), gg, pp))
print(fieldGaluefindOne(ff, pp))
print(fieldGalueTrace(hh, pp))'''
'''
sumGF = fieldGalueAdd(gg, ff)
sumGFmulH = fieldGalueMul(sumGF, hh, pp)
mulHsumGF = fieldGalueMul(hh, sumGF, pp)
mulGH = fieldGalueMul(gg, hh, pp)
mulFH = fieldGalueMul(ff, hh, pp)
sumMulGHmulFH = fieldGalueAdd(mulGH, mulFH)
if sumMulGHmulFH == mulHsumGF == sumGFmulH:
    print('Success')
else:
    print('Error')
power = stringToArray(bin(2**m - 1)[2:])
fToPower = fieldGaluePower(ff, power, pp)
if fToPower == [1]:
    print('Success')
else:
    print('Error')

def timeSearch(f, *args, repeats=10):
    start = time.perf_counter()
    for _ in range(repeats):
        f(*args)
    end = time.perf_counter()
    avg_time = (end - start) / repeats
    return avg_time  

avg = timeSearch(fieldGaluefindZero, ff)
print(f"Середній час роботи fieldGaluefindZero: {avg:.10f} сек")
avg1 = timeSearch(fieldGaluefindOne, ff, pp)
print(f"Середній час роботи fieldGaluefindOne: {avg1:.10f} сек")
avg2 = timeSearch(fieldGalueAdd, gg, ff)
print(f"Середній час роботи fieldGalueAdd: {avg2:.10f} сек")
avg3 = timeSearch(fieldGalueMul, gg, ff, pp)
print(f"Середній час роботи fieldGalueMul: {avg3:.10f} сек")
avg4 = timeSearch(fieldGalueTrace, gg, pp)
print(f"Середній час роботи fieldGalueTrace: {avg4:.10f} сек")
avg5 = timeSearch(fieldGalueSquarePower, gg, pp)
print(f"Середній час роботи fieldGalueSquarePower: {avg5:.10f} сек")
avg6 = timeSearch(fieldGaluePower, gg, ff, pp)
print(f"Середній час роботи fieldGaluePower: {avg6:.10f} сек")
avg7 = timeSearch(fieldGalueInverseElement, gg, pp)
print(f"Середній час роботи fieldGalueInverseElement: {avg7:.10f} сек")
avg8 = timeSearch(stringToArray, g)
print(f"Середній час роботи stringToArray: {avg8:.10f} сек")
avg9 = timeSearch(arrayToString, gg)
print(f"Середній час роботи arrayToString: {avg9:.10f} сек")'''
