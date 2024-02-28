import math

def solve_quadratic_equation(a, b, c):
    delta = b**2 - 4*a*c

    #檢查 
    if delta > 0:
        root1 = (-b + math.sqrt(delta)) / (2*a)
        root2 = (-b - math.sqrt(delta)) / (2*a)
        return root1, root2
    elif delta == 0:
        root = -b / (2*a)
        return root,
    else:
        real_part = -b / (2*a)
        unknow_part = math.sqrt(abs(delta)) / (2*a)
        root1 = complex(real_part, unknow_part)
        root2 = complex(real_part, unknow_part)
        return root1, root2

a = float(input("輸入a的值: "))
b = float(input("輸入b的值: "))
c = float(input("輸入c的值: "))

roots = solve_quadratic_equation(a, b, c)
#輸出
print(roots)
