from datetime import datetime
import pytz

input_str = "Mon 26/05/2025 11:51 AM"  # update IST time with day and time
print("IST Time:", input_str)

ist_format = "%a %d/%m/%Y %I:%M %p"
ist_time = datetime.strptime(input_str, ist_format)

ist_zone = pytz.timezone("Asia/Kolkata")
ist_time = ist_zone.localize(ist_time)

cst_zone = pytz.timezone("US/Central")
cst_time = ist_time.astimezone(cst_zone)

output_str = cst_time.strftime("%a %d/%m/%Y %I:%M %p")
print("CST TIME:", output_str)
