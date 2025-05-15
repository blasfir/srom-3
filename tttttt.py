m = 233
p = '10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010001011'

def stringToArray(n):
    result = result = list(map(int, n))
    result = deleteExtraZeros(result)
    return result

def make_eq(A, B):
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

def galueAdd(A, B):
    A = deleteExtraZeros(A)
    B = deleteExtraZeros(B)
    A, B = make_eq(A, B)
    result = []
    for i in range(len(A)):
        k = int(A[i]) + int(B[i])
        n = k % 2
        result.append(n)
    result = deleteExtraZeros(result)    
    return result

def galueModule(A, N):
    A = deleteExtraZeros(A)
    N = deleteExtraZeros(N)
    if len(A) < len(N):
        return A

    shift = len(A) - len(N)
    N_shifted = N + [0] * shift  # зсуваємо N вправо до ступеня A

    A, N_shifted = make_eq(A, N_shifted)
    for i in range(len(A)):
        A[i] = (A[i] + N_shifted[i]) % 2

    A = deleteExtraZeros(A)
    return galueModule(A, N)

def galueMultiply(A, B, N):
    A = deleteExtraZeros(A)
    B = deleteExtraZeros(B)
    A, B = make_eq(A, B)
    result = [0] * (len(A) * 2 - 1)
    for i in range(len(A)):
        if A[i] == 1:
            for j in range(len(B)):
                result[i+j] = (result[i+j] + B[j]) % 2
    result = galueModule(result, N)            
    return deleteExtraZeros(result)

def galueSquare(a, p_x):
    res = galueMultiply(a, a, p_x)
    return res

def galuePower(a, n, p_x):
    res = [1]
    for i in n:
        if i == 1:
            res, a = make_eq(res, a)
            res = galueMultiply(res, a, p_x)
        a = galueSquare(a, p_x)
    return res

def galueInverse(a, p_x):
    m_new = bin(2**m - 2)[2:]
    m1 = []
    for i in m_new:
        m1.append(int(i))
    m1 = m1[::-1]
    res = galuePower(a, m1, p_x)
    return res

def galueTrace(a, m, p_x):
    tr = a
    temp = a
    for i in range(m):
        temp = galueSquare(temp, p_x)
        tr, temp = make_eq(tr, temp)
        tr = galueAdd(tr, temp)
    return sum(tr) % 2

def findZero(a):
    return galueAdd(a, a)

def findOne(a, m, p_x):
    a_inv = galueInverse(a, p_x)
    a_inv, a = make_eq(a_inv, a)
    neutral = galueMultiply(a, a_inv, p_x)
    return neutral

def converter(n, m):
    if len(n) > 233:
        while len(n) != 233:
            n.pop(0)
    n = [str(i) for i in n]
    while len(n) < 233:
        n = ['0'] + n
    return ''.join(n)

f = '11001000010110010111101001000011001011001000010000010110110100110111010101001111000111001101001111110011111101000101011110110110111011000110001101001001100111111001111000001011101010001110110100110101011100101110101010011100010101011'
g = '10101011011111010100001001100011100110010010100001001101110010110010111000010110010001101001010101001011011110101000110001001110101111101010100100101011010000011101010011011000001011010111001000010001010010000010101100111000100101001'
h = '10110010110100100100110111110001111001101010100010000001011000101110111111001111000100000110010111110001110101000011111111011101101001101101111010000001101100000110001111110011101010110011010111000100010101110111100100010000001100010'
#f = '1000100000000000000000001111111111111111111111111111111111111111111111111111000000000000000000000000000000000000011111111111111111111111111'
#g = '1010101'
#h = '10'
pp = stringToArray(p)
ff = stringToArray(f)
gg = stringToArray(g)
hh = stringToArray(h)
#print(arrayToString(ff))
#print(fieldGalueAdd(ff, gg))
#print(fieldGalueModule(ff, pp))
#print(fieldGalueMul(ff, gg, pp))
#print(inverted_element(ff))
#print(fieldGaluePower(gg, hh, pp))
#print(fieldGalueInverseElement(gg, pp))
#print(fieldGaluefindOne(ff, pp))
#print(fieldGalueMul(fieldGalueInverseElement(gg, pp), gg, pp))
#print(fieldGaluefindOne(ff, pp))
#print(fieldGalueTrace(hh, pp))
'''sumGF = fieldGalueAdd(gg, ff)
sumGFmulM = fieldGalueMul(sumGF, hh, pp)
mulMsumGF = fieldGalueMul(hh, sumGF, pp)
mulGM = fieldGalueMul(gg, hh, pp)
mulFM = fieldGalueMul(ff, hh, pp)
sumMulGMmulFM = fieldGalueAdd(mulGM, mulFM)
if sumMulGMmulFM == mulMsumGF == sumGFmulM:
    print('Success')
else:
    print('Error')'''
print(galueMultiply(galueInverse(gg, pp), gg, pp))







'''
a = '11001000010110010111101001000011001011001000010000010110110100110111010101001111000111001101001111110011111101000101011110110110111011000110001101001001100111111001111000001011101010001110110100110101011100101110101010011100010101011'
b = '10101011011111010100001001100011100110010010100001001101110010110010111000010110010001101001010101001011011110101000110001001110101111101010100100101011010000011101010011011000001011010111001000010001010010000010101100111000100101001'
n = '10110010110100100100110111110001111001101010100010000001011000101110111111001111000100000110010111110001110101000011111111011101101001101101111010000001101100000110001111110011101010110011010111000100010101110111100100010000001100010'

# p(x) = x**233 + x**9 + x**4 + x + 1
p_x = '100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000010011'

p = stringToArray(p_x)

a1 = stringToArray(a)
b1 = stringToArray(b)


a1, b1 = make_eq(a1, b1)
print(galueMultiply(galueInverse(a1, p), a1, p))'''
'''print()
galAdd = galueAdd(a1, b1)
print(f'A + B = {converter(galAdd, m)}')
print()
galMul = galueMultiply(a1, b1, p)
print(f'A * B = {converter(galMul, m)}')
print()
galSquare = galueSquare(a1, p)
print(f'A ^ 2 = {converter(galSquare, m)}')

n1 = []
for i in n:
    n1.append(int(i))
n1 = n1[::-1]

print()
galInv = galueInverse(a1, m, p)
print(f'A ^-1 = {converter(galInv, m)}')

print()
galPow = galuePower(a1, n1, p)
print(f'A ^ N = {converter(galPow, m)}')


'''
'''print()
print('***********************TESTING***********************')
print()

def test1(a, b, c, p_x, m):
    add1 = galueAdd(a, b)
    mul1 = galueMultiply(add1, c, p_x)
    mul2 = galueMultiply(b, c, p_x)
    mul3 = galueMultiply(c, a, p_x)
    s = [0] * m
    mul1, s = make_eq(mul1, s)
    mul2, s = make_eq(mul2, s)
    mul3, s = make_eq(mul3, s)
    add2 = galueAdd(mul2, mul3)
    if mul1 == add2:
        return '(a + b) * c = b * c + c * a - True'
    
    

at = '00110110101100100110110011111001010101111101101101001110101010101100010010011111100010111111000110011010110110101100011101010011100110001111010100001001100101011010000010001001001010101000000001101111011010110110101110000011011000001'
bt = '01111110111001010000110110111110110010000000101001001110110101100000000010110111010100011011001101001011001010100101000000011101100100111100000100111010010010101001100100001001101010100100010000110000001100110010001010101111000101110'
ct = '00110101000100010100001100000001101101000010101000111111101101011010010011100000000101000010010101000010010000011100010011101000101100010011011000110100000100010010110111101000100101110010100100111010110011100000001111111001010101111'

at1 = []
for i in at:
    at1.append(int(i))


bt1 = []
for i in bt:
    bt1.append(int(i))

ct1 = []
for i in ct:
    ct1.append(int(i))

print(test1(at1, bt1, ct1, p, m))


def test2(d, p, m):
    m_new = bin(2**m - 1)[2:]
    m1 = []
    for i in m_new:
        m1.append(int(i))
    m1 = m1[::-1]
    res = galuePower(d, m1, p)
    while len(res) > 1:
        res.pop(0)
    if res == [1]:
        return 'd^(2**m - 1) = 1 - True'


d = '01110010010001101101011000100111011011010011100111101001010101110110100001100000001110110101001010111110011010000101011110110001101011101001111111000101000000000101110101011111011000001111001101001110101100010000100100110101010110101'
d1 = []
for i in d:
    d1.append(int(i))


print(test2(d1, p, m))

print()
print('***********************TIME TESTING***********************')
print()

def random_polynom(m):
    while True:
        pol = ''.join(random.choice('01') for i in range(m))
        if '0' in pol and '1' in pol and pol[0] == '1':
            return pol
        

def AverageTimeLongTest(n, operation):
    average_time = []
    p_x = '100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000010011'
    p = []
    for i in p_x:
        p.append(int(i))
    for _ in range(n):
        a = random_polynom(233)
        b = random_polynom(233)
        pow = random_polynom(233)
        a1 = []
        b1 = []
        for i in a:
            a1.append(int(i))

        for i in b:
            b1.append(int(i))

        n1 = []
        for i in pow:
            n1.append(int(i))
        n1 = n1[::-1]    
        
        if operation == 'galueAdd':
            start = time.time()    
            res = galueAdd(a1, b1)
            end = time.time()
            final_time = end - start
            average_time.append(final_time)
        elif operation == 'galueProduct':
            start = time.time()
            res = galueMultiply(a1, b1, p)
            end = time.time()
            final_time = end - start
            average_time.append(final_time)
        elif operation == 'galueSquare':
            start = time.time()
            res = galueSquare(a1, p)
            end = time.time()
            final_time = end - start
            average_time.append(final_time)
        elif operation == 'galueInverse':
            start = time.time()
            res = galueInverse(a1, 233, p)
            end = time.time()
            final_time = end - start
            average_time.append(final_time)
        elif operation == 'galuePower':
            start = time.time()
            res = galuePower(a1, n1, p)
            end = time.time()
            final_time = end - start
            average_time.append(final_time)
        return (sum(average_time))/len(average_time)
    


GalAddTime100 = AverageTimeLongTest(100, 'galueAdd')
GalAddTime1000 = AverageTimeLongTest(1000, 'galueAdd')
GalAddTime10000 = AverageTimeLongTest(10000, 'galueAdd')

GalProductTime100 = AverageTimeLongTest(100, 'galueProduct')
GalProductTime1000 = AverageTimeLongTest(1000, 'galueProduct')
GalProductTime10000 = AverageTimeLongTest(10000, 'galueProduct')

GalSqTime100 = AverageTimeLongTest(100, 'galueSquare')
GalSqTime1000 = AverageTimeLongTest(1000, 'galueSquare')
GalSqTime10000 = AverageTimeLongTest(10000, 'galueSquare')

GalInvTime100 = AverageTimeLongTest(100, 'galueInverse')
GalInvTime1000 = AverageTimeLongTest(1000, 'galueInverse')
GalInvTime10000 = AverageTimeLongTest(10000, 'galueInverse')

GalPowTime100 = AverageTimeLongTest(100, 'galuePower')
GalPowTime1000 = AverageTimeLongTest(1000, 'galuePower')
GalPowTime10000 = AverageTimeLongTest(10000, 'galuePower')

timeResultsAll = {'100 ітерацій': [f"{GalAddTime100:.20f}", f"{GalProductTime100:.20f}", f"{GalSqTime100:.20f}", f'{GalInvTime100:.20f}', f'{GalPowTime100:.20f}'],
                  '1000 ітерацій': [f"{GalAddTime1000:.20f}", f"{GalProductTime1000:.20f}", f"{GalSqTime1000:.20f}", f'{GalInvTime1000:.20f}', f'{GalPowTime1000:.20f}'],
                  '10000 ітерацій' : [f"{GalAddTime10000:.20f}", f"{GalProductTime10000:.20f}", f"{GalSqTime10000:.20f}", f'{GalInvTime10000:.20f}', f'{GalPowTime10000:.20f}']}

df = pd.DataFrame(timeResultsAll, index=['galueAdd', 'galueProduct', 'galueSquare', 'galueInverse', 'galuePower'])

print(df)
'''