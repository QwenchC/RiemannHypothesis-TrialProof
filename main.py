import mpmath

# 设置高精度
mpmath.mp.dps = 50  # 小数点后位数

# 定义 θ 函数
def theta(t):
    return mpmath.im(mpmath.loggamma(0.25 + 0.5j * t)) - t * mpmath.log(mpmath.pi) / 2

# 定义 Z 函数
def Z(t):
    return mpmath.re(mpmath.exp(1j * theta(t)) * mpmath.zeta(0.5 + 1j * t))

# 寻找零点
t_min = 0
t_max = 50
t_values = mpmath.linspace(t_min, t_max, 1000)
previous_value = Z(t_values[0])

for t in t_values[1:]:
    current_value = Z(t)
    if previous_value * current_value < 0:
        # 零点在 (t_prev, t) 之间
        zero = mpmath.findroot(Z, t, solver='muller')
        print(f"Found zero at t = {zero}")
    previous_value = current_value
