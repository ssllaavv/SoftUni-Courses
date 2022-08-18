meerkat = []
for i in range(3):
    meerkat.append(input())
meerkat[2], meerkat[0] = meerkat[0], meerkat[2]
print(meerkat)
