l = 0
r = 1.5
run_count = 0
x = l
n0 = x**3 - 1.8 * x**2 - 1.2 * x + 1.6
print(n0)

x = r
n0 = x**3 - 1.8 * x**2 - 1.2 * x + 1.6
print(n0)

x = (l+r)/2
n0 = x**3 - 1.8 * x**2 - 1.2 * x + 1.6
l = x

while abs(n0) > 0.01:
    x = (l+r)/2
    n0 = x**3 - 1.8 * x**2 - 1.2 * x + 1.6
    r = x
    run_count = run_count + 1
    print(n0)

print(x)
print(run_count)