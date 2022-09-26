xa = float(input('Введите координату точки A по X: '))
ya = float(input('Введите координату точки A по Y: '))
xb = float(input('Введите координату точки B по X: '))
yb = float(input('Введите координату точки B по Y: '))
dist = ((xb - xa)**2 + (ya - yb)**2)**0.5
print('Расстояние между точками A и B равно', round(dist, 2))