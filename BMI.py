height = input('請輸入身高: ')
body_weight = input('請輸入體重: ')
height = float(height)
body_weight = float(body_weight)
BMI = (body_weight) / ( ( height / 100 ) * ( height / 100 ) )
print('你的BMI是: ', BMI)
if BMI < 18.5 :
	print('你體重過輕了')
elif BMI >= 18.5 and BMI < 24:
	print('你屬於正常範圍')
elif BMI >= 24 and BMI < 27:
	print('你體重過重了')
elif BMI >= 27 and BMI < 30:
	print('你屬於輕度肥胖')
elif BMI >= 30 and BMI < 35:
	print('你屬於輕度肥胖')
else:
	print('你屬於重度肥胖')
	
	
	