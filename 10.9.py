txt = 'Прив3т, т4 д3лал чт0-то се4одня?567'
nums = []
nums_sum = 0
for i in txt:
    if i in '1234567890':
        nums.append(int(i))
        nums_sum += int(i)
print('Все цифры в тексте: ', nums,'Сумма цифр в тексте: ', nums_sum, 'Максимальное число в тексте: ', max(nums))