tweet='Hello earth! I am here in your earth'
print(tweet[:6]) #first positon theke koto dur print korte chai

print(tweet[-7:])
print(tweet[6:14])


messey="Visit##eerirt!!! it is so greeen"

cleaned = messey.replace('#',' ').replace('!','')
print(cleaned)

text=' Nayeem is a lion'
text=text.upper()
text=text.lower()
text=text.capitalize()
text=text.title()
print(text)

seperate='Nayeem try to split a text the'
seperate=seperate.split('the')
print(seperate)


planet='Earth'
tem=234.4
weather= 'rainy'
report='Planet : {},tem: {:.2f},weather:{}'.format(planet,tem,weather)
print(report)


mass=35.22
print(f'My mass is {mass:.2f} kg') 
print(report.count('a'))