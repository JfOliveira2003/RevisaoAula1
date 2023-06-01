def calculadora(a, b, p)
	p = input('Qual tipo de operação deseja realizar? ').upper()	
	if p == 'SOMA':
		print('a soma será: ', a + b)
	if p == 'SUBTRAÇÃO':
		print('A subtração será: ', a - b)
	if p == 'MULTIPLICAÇÃO':
		print('A multiplicação será: ', a * b)
	if p == 'DIVISÃO':
		print('A divisão será: ', a / b)

