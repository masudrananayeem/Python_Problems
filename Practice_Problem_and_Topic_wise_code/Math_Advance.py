import math

distance_to_home = 3222
gravity=9.8

thurst_need = math.sqrt(gravity*distance_to_home)
print('Thurst Needed',thurst_need)

height=115
base_lenght=10
angle_radiu=math.atan(height/base_lenght)
print(angle_radiu)
angle_radiu=math.degrees(angle_radiu)
print('Degree value : ',angle_radiu)

print('rounded angle',round(angle_radiu))

angle_radiu=32.23
print('celling :' , math.ceil(angle_radiu))
print('floor',math.floor(angle_radiu))

