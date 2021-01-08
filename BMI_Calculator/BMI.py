height = input('請輸入身高(公尺): ')
weight = input('請輸入體重(公斤): ')
height = float(height)
weight = float(weight)
BMI = weight / (height * height)
BMI = float(BMI)
if BMI < 18.5:
    print('您的BMI值為:', BMI, '體重過輕')
elif 18.5 <= BMI and BMI < 24:
    print('您的BMI值為:', BMI, '正常範圍')
elif 24 <= BMI and BMI < 27:
    print('您的BMI值為:', BMI, '過重')
elif 27 <= BMI and BMI < 30:
    print('您的BMI值為:', BMI, '輕度肥胖')
elif 30 <= BMI and BMI < 35:
    print('您的BMI值為:', BMI, '中度肥胖')
else:
    print('您的BMI值為:', BMI, '重度肥胖')