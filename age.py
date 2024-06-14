driving = input('請問你有開過車嗎 ')
if driving != '有' and driving != '沒有':
	print('只能輸入有跟沒有別來亂')
	raise SystemExit
age = input('請問你幾歲')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過考驗')
	else:
		print('奇怪 你怎麼可以開車')
elif driving == '沒有':
	if age >= 18:
		print('你怎麼不去考駕照')
	else:
		print('沒事啦 再過幾年你就可以考駕照了')
