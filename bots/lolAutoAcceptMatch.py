import pyautogui
import pygetwindow as gw
import time
import threading
import win32gui
import sys

def bring_window_to_foreground(window_title):
    """
    Brings the specified window to the foreground if it exists.
    
    :param window_title: The title of the window to bring to the foreground
    """
    try:
        windows = gw.getWindowsWithTitle(window_title)
        if windows:
            window = windows[0]
            hwnd = win32gui.FindWindow(None, window.title)
            if hwnd:
                win32gui.SetForegroundWindow(hwnd)
                print(f"Window '{window_title}' brought to the foreground.")
    except Exception as e:
        print(f"Error bringing window to foreground: {e}")

def monitor_and_click(target_window_title, x_offset=10, y_offset=10, check_interval=1, stop_event=None):
    """
    Continuously monitors for the appearance of a window with the given title and clicks it when found and in the foreground.

    :param target_window_title: Title of the window to monitor
    :param x_offset: X-offset in pixels from the window's top-left corner for the click
    :param y_offset: Y-offset in pixels from the window's top-left corner for the click
    :param check_interval: Time (in seconds) between checks for the window
    :param stop_event: Threading Event object to gracefully stop the loop
    """
    print(f"Monitoring for window: '{target_window_title}'...")

    while not stop_event.is_set():  # Check the stop_event to allow graceful exit
        # Look for the target window
        windows = gw.getWindowsWithTitle(target_window_title)
        if windows:
            window = windows[0]  # Take the first matching window
            bring_window_to_foreground(target_window_title)  # Ensure the window is in the foreground

            if is_window_in_foreground(target_window_title):

                x = window.left + x_offset
                y = window.top + y_offset

                pyautogui.moveTo(x, y, duration=0.5)  # Smooth movement to position
                pyautogui.click()



        time.sleep(check_interval)  # Wait before checking again

def is_window_in_foreground(window_title):
    """
    Checks if the specified window title matches the current foreground window.
    
    :param window_title: The title of the window to check
    :return: True if the window is in the foreground, False otherwise
    """
    try:
        foreground_window = win32gui.GetForegroundWindow()
        active_window_title = win32gui.GetWindowText(foreground_window)
        return active_window_title == window_title
    except Exception as e:
        print(f"Error checking foreground window: {e}")
        return False


if __name__ == "__main__":
    # Define the target window title
    target_window_title = "League of Legends"

    # Offset for clicking inside the window
    x_offset = 100
    y_offset = 100

    # Interval to check for the window
    check_interval = 1  # 1 second

    # Create a stop event for the background thread
    stop_event = threading.Event()

    # Run the monitor in a background thread
    bot_thread = threading.Thread(target=monitor_and_click, args=(target_window_title, x_offset, y_offset, check_interval, stop_event))
    bot_thread.start()

