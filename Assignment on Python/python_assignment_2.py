import psutil
import time

# Define the CPU usage threshold (e.g., 80%)
threshold = 80

print("Monitoring CPU usage...")

try:
    while True:
        # Get the current CPU usage as a percentage
        cpu_percent = psutil.cpu_percent()

        # Check if CPU usage exceeds the threshold
        if cpu_percent > threshold:
            print("Alert! CPU usage exceeds threshold:", cpu_percent, "%")

        # Wait for a few seconds before checking again
        time.sleep(5)

except KeyboardInterrupt:
    print("Monitoring stopped by the user.")
except Exception as e:
    print("An error occurred:", e)
