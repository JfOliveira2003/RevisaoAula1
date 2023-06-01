def calculadora(a, b):
	p = input('Qual tipo de operação deseja realizar? ').upper()	
	if p == 'SOMA':
		print('A soma será: ', a + b)
	if p == 'SUBTRAÇÃO':
		print('A subtração será: ', a - b)
	if p == 'MULTIPLICAÇÃO':
		print('A multiplicação será: ', a * b)
	if p == 'DIVISÃO':
		print('A divisão será: ', a / b)
		

print('='*25, 'CALCULADORA SIMPLES', '='*25)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
calculadora(n1, n2)



