# Task 13
# Виведіть на екран «пісочний годинник», максимальна ширина якого зчитується з клавіатури (число непарне).
# У прикладі ширина дорівнює 5.
# *****
#  ***
#   *
#  ***
# *****

x=int(input("Введіть ширину ="))
from itertools import chain
print("\n".join(chain((('* ' * i + '*').rjust(x * 2 + i) for i in range((x-1), 0, -1)), (('* ' * i + '*').rjust(x * 2 + i) for i in range(x)))))