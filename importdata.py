import matplotlib.pyplot as plt

raw = []
x = []
y = []

with open("TRAIN10X.DAT") as file:
    for line in file:
        raw.append(line.rstrip('\n\r '))
i = 0
while i < len(raw):
    if raw[i] != '':
        x.append(raw[i])
        y.append(raw[i+2])
        i += 5
print(x)
print(y)
