distance = int(input())
fivesteps = int(distance/5)
foursteps = int((distance%5)/4)
threesteps = int(((distance%5)%4)/3)
twosteps = int((((distance%5)%4)%3)/2)
onesteps = int((((distance%5)%4)%3)%2)
print(fivesteps+foursteps+threesteps+twosteps+onesteps)