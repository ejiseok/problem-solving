scale = list(map(int, input().split()))

asc_or_dsc = True

for i in range(len(scale) - 1):
    if abs(scale[i] - scale[i + 1]) != 1:
        asc_or_dsc = False
        break

if asc_or_dsc:
    print("ascending" if scale[0] == 1 else "descending")
else:
    print("mixed")