
equation = '-12+12-7979+9191'
l=[int(i) for i in ('0'+equation).replace('-','+-').split('+')]
print(l)