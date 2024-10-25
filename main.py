import pywhatkit
import pyautogui
import time

try:
    # Schedule the message to be sent (adjust the time accordingly)
    pywhatkit.sendwhatmsg("+573200000", "Hello Python", 11, 00)


    # Simulate pressing 'Enter' key to send the message
    pyautogui.press("enter")
    # Wait a few seconds to ensure WhatsApp Web loads and the message appears
    time.sleep(5)  # Adjust if needed, depending on your internet speed


    print("Message sent successfully!")

except Exception as e:
    print(f"An error occurred: {e}")