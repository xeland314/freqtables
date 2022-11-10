from lib import FreqTableSimple

tabla1 = FreqTableSimple([
    'A', 'A', 'A', 'B', 'B',
    'B', 'B', 'B', 'B', 'C'
])
tabla2 = FreqTableSimple({
    'A':3, 'B':6, 'C':1
})
tabla3 = FreqTableSimple(
    'A', 'A', 'A', 'B', 'B',
    'B', 'B', 'B', 'B', 'C'
)
tabla4 = FreqTableSimple(
    A = 3, B = 6, C = 1
)

print(tabla1)