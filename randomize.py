from os import scandir, rename
from random import randrange
from re import match

path = r'.\xyz'
res = []
rand = []

for v in scandir(path):
  res.append(v.name)
c = len(res) + 1
for name in res:
  while True:
    r = randrange(1, len(res) + 1)
    if r in rand:
      continue
    else:
      rand.append(r)
      break
  old = path + '\\' + name
  if bool(match('[0-9]{3}_', name)):
    name = name[4:]
  rename(old, path + '\\' + str(r).rjust(3, '0') + '_' + name)
  #rename(v, v[:len(v) - 1])
res.clear()
for v in scandir(path):
  res.append(v.name)
res.sort()
print('New files\' names:\n')
for v in res:
  print(v)
