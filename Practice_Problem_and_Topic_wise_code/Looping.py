donuts=['glazed','chocolate','galactic sprinkle','nut']

for x in donuts:
    print(x)


angle= 0
while angle<90:
    print('Angle: ',angle)
    angle=angle+30


for i in range(1, 11, 2):
    print(i)


protocol=['ok', 'ok', 'bad', 'bad','ok']
for i , protocol in enumerate(protocol):
    print(i,protocol)
    if protocol=='bad':
        break
