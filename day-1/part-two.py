f = open("input.txt", "r")

elf_cal = []
temp_elf_sum = 0

for item in f:
    try:
        cal_item = int(item)

        temp_elf_sum = temp_elf_sum + cal_item
        print('Line', item)
        print('Type', cal_item)
    except:
        elf_cal.append(temp_elf_sum)
        temp_elf_sum = 0
        print("End")

elf_cal = sorted(elf_cal, reverse=True)
print('Elf with max cal has ', elf_cal[0] + elf_cal[1] + elf_cal[2])
