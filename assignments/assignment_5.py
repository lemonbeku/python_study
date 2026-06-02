def computepay(h, r):
    if(h > 0 and h <=40):
        total_rate = h * r
    elif(h > 40):
        tratefirst = 40 * r
        h_fix = h - 40
        total_rate = (h_fix * r * 1.5) + tratefirst

    return total_rate

hrs = float(input("Enter Hours:"))
rph = float(input("Enter rate per hour:"))
p = computepay(hrs, rph)
print("Pay", p)
