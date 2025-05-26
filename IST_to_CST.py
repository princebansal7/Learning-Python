from datetime import datetime
import pytz

# Define input
input_str = "Sun 25/05/2025 9:43 am"

# Step 1: Parse input to datetime object
ist_format = "%a %d/%m/%Y %I:%M %p"
ist_time = datetime.strptime(input_str, ist_format)

# Step 2: Set timezone to IST
ist_zone = pytz.timezone("Asia/Kolkata")
ist_time = ist_zone.localize(ist_time)

# Step 3: Convert to CST (US Central Standard Time)
cst_zone = pytz.timezone("US/Central")
cst_time = ist_time.astimezone(cst_zone)

# Step 4: Format the output as required
output_str = cst_time.strftime("%a %d/%m/%Y %I:%M %p")
print(output_str)
