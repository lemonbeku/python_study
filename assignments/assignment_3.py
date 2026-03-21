hrs = input("Enter Hours:")
rph = input("Enter Rate Per Hour:")

h = float(hrs)
r =float(rph)
add_r = r * 1.5

if h <= 40:
    final = h * r
elif h > 40:
    extra_h = h - 40
    final = (40 * r) + (extra_h * add_r)
    
print(final)
