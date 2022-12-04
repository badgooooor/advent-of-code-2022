f = open("input.txt", "r")

elf_with_max_cal = 0
temp_elf_sum = 0

for item in f:
    try:
        cal_item = int(item)

        temp_elf_sum = temp_elf_sum + cal_item
        print('Line', item)
        print('Type', cal_item)
    except:
        if temp_elf_sum > elf_with_max_cal:
            elf_with_max_cal = temp_elf_sum
        temp_elf_sum = 0
        print("End")

print('Elf with max cal has ', elf_with_max_cal)
