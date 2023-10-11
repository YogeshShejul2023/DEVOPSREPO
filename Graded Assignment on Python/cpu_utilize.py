import psutil
import time

# Predefined CPU usage threshold (e.g., 80%)
threshold = 80

print("Monitoring CPU usage...")

try:
    while True:
        # Get the current CPU usage as a percentage
        cpu_usage = psutil.cpu_percent(interval=1)

        # Check if CPU usage exceeds the threshold
        if cpu_usage > threshold:
            print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")

        # Wait for a moment before checking again
        time.sleep(1)

except KeyboardInterrupt:
    print("\nMonitoring stopped. Exiting...")
except Exception as e:
    print(f"An error occurred: {str(e)}")
