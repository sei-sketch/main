from pypresence import Presence
import time

# Your Discord application's Client ID
CLIENT_ID = "YOUR_CLIENT_ID"  # Replace with your own

# Connect to Discord
rpc = Presence(CLIENT_ID)
rpc.connect()

# Simulate impossible playtime: 50 years ago
start_time = int(time.time()) - (50 * 365 * 24 * 60 * 60)

# Update the Rich Presence
rpc.update(
    large_image="Image_Key",
    small_image="Small_Key",      # Optional small GIF
    start=start_time             # Impossible playtime
)

print("WAG MO 'TO ICLOSE TANGINA KA")
print("@northside.sev")

# Keep the script alive
try:
    while True:
        time.sleep(15)
except KeyboardInterrupt:
    print("\nDisconnected from Discord.")
    rpc.clear()
