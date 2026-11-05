import math


def relative_error(approx, exact):
    return abs(approx - exact) / abs(exact)

def absolute_error(approx, exact):
    return abs(approx - exact)


pi_approx = 3.14
pi_exact = math.pi

d_pi = absolute_error(pi_approx, pi_exact)
rel_pi = relative_error(pi_approx, pi_exact)

print("1) pi vs 3.14:")
print("   Абсолютная:", d_pi)
print("   Относительная:", rel_pi, f"({rel_pi * 100:.4f}%)")


sum_approx = 0.1 + 0.2
sum_exact = 0.3

d_sum = absolute_error(sum_approx, sum_exact)
rel_sum = relative_error(sum_approx, sum_exact)

print("\n2) (0.1 + 0.2) vs 0.3:")
print("   Абсолютная:", d_sum)
print("   Относительная:", rel_sum)


arr = [0.1] * 1_000_000
loop_sum = sum(arr)
fsum_val = math.fsum(arr)

d_loop = absolute_error(loop_sum, fsum_val)
rel_loop = relative_error(loop_sum, fsum_val)

print("\n3) Сумма 1 млн элементов:")
print("   Обычный sum():", loop_sum)
print("   math.fsum():  ", fsum_val)
print("   Абсолютная:   ", d_loop)
print("   Относительная:", rel_loop)
