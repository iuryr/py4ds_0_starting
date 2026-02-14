import time

seconds_since_epoch = time.time()
time_struct = time.gmtime(seconds_since_epoch)
month_day_year = time.strftime("%b %d %Y", time_struct)

print(f"Seconds since January 1st, 1970: {seconds_since_epoch:,.4f} or {seconds_since_epoch:.2e} in scientific notation")
print(month_day_year)
