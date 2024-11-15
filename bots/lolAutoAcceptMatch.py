import pyautogui
import pygetwindow as gw
import time
import threading

def monitor_and_click(target_window_title, x_offset=10, y_offset=10, check_interval=1):
    """
    Monitors for the appearance of a window with the given title and clicks it when found.

    :param target_window_title: Title of the window to monitor
    :param x_offset: X-offset in pixels from the window's top-left corner for the click
    :param y_offset: Y-offset in pixels from the window's top-left corner for the click
    :param check_interval: Time (in seconds) between checks for the window
    """
    print(f"Monitoring for window: '{target_window_title}'...")

    while True:

        windows = gw.getWindowsWithTitle(target_window_title)
        if windows:
            window = windows[0]  
            print(f"Window found: '{window.title}'")


            window.activate()


            x = window.left + x_offset
            y = window.top + y_offset


            print(f"Clicking at ({x}, {y})")
            pyautogui.moveTo(x, y, duration=0.5) 
            pyautogui.click()


            break

        time.sleep(check_interval) 


if __name__ == "__main__":

    target_window_title = "League of Legends"


    x_offset = 100
    y_offset = 100


    check_interval = 1  # 1 second

    bot_thread = threading.Thread(target=monitor_and_click, args=(target_window_title, x_offset, y_offset, check_interval))
    bot_thread.daemon = True  
    bot_thread.start()

    print("Bot is running in the background. Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(1)  
    except KeyboardInterrupt:
        print("\nBot stopped.")