"""
Keylogger Log Analyzer - Educational Edition
Author: Darshan Gholap (for Prodigy Infotech Internship Task)
Purpose: Analyze keylogs.csv and generate session statistics.

⚠️ Use only with self-generated logs for ethical demonstration.
"""

import csv
import os
import datetime
from collections import Counter

# ==========================================================
# CONFIGURATION
# ==========================================================
LOG_DIR = "keylogs"
LOG_FILE = os.path.join(LOG_DIR, "keylog.csv")
SUMMARY_FILE = os.path.join(LOG_DIR, "summary.csv")


# ==========================================================
# UTILITY FUNCTIONS
# ==========================================================
def load_logs(file_path):
    """Load keylog CSV data safely."""
    if not os.path.exists(file_path):
        print(f"❌ Error: {file_path} not found. Run keylogger_csv.py first.")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            logs = list(reader)
            return logs
    except Exception as e:
        print(f"⚠️ Failed to read CSV file: {e}")
        return []


def parse_timestamp(ts):
    """Convert timestamp string to datetime object."""
    try:
        return datetime.datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
    except Exception:
        return None


# ==========================================================
# ANALYSIS FUNCTIONS
# ==========================================================
def summarize_logs(logs):
    """Compute total key counts, session duration, and top keys."""
    if not logs:
        print("⚠️ No valid log entries found to analyze.")
        return None

    pressed_counter = Counter()
    released_counter = Counter()
    timestamps = []

    for entry in logs:
        key = entry.get("Key", "Unknown")
        action = entry.get("Action", "").strip().upper()
        ts = parse_timestamp(entry.get("Timestamp", ""))
        if ts:
            timestamps.append(ts)

        if action == "PRESSED":
            pressed_counter[key] += 1
        elif action == "RELEASED":
            released_counter[key] += 1

    total_pressed = sum(pressed_counter.values())
    total_released = sum(released_counter.values())

    session_start = min(timestamps) if timestamps else None
    session_end = max(timestamps) if timestamps else None
    duration = (session_end - session_start) if (session_start and session_end) else None

    top_keys = pressed_counter.most_common(10)

    return {
        "total_pressed": total_pressed,
        "total_released": total_released,
        "session_start": session_start,
        "session_end": session_end,
        "duration": duration,
        "top_keys": top_keys,
    }


def export_summary(summary):
    """Save key statistics into a summary CSV."""
    try:
        with open(SUMMARY_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Metric", "Value"])
            writer.writerow(["Total Keys Pressed", summary["total_pressed"]])
            writer.writerow(["Total Keys Released", summary["total_released"]])
            writer.writerow(["Session Start", summary["session_start"]])
            writer.writerow(["Session End", summary["session_end"]])
            writer.writerow(["Duration", str(summary["duration"])])
            writer.writerow([])
            writer.writerow(["Top 10 Keys", "Press Count"])
            for key, count in summary["top_keys"]:
                writer.writerow([key, count])

        print(f"\n✅ Summary exported successfully to: {SUMMARY_FILE}")
    except Exception as e:
        print(f"⚠️ Failed to export summary: {e}")


def print_summary(summary):
    """Display analysis in a formatted console view."""
    print("\n" + "=" * 65)
    print("📊  KEYLOGGER SESSION ANALYSIS REPORT")
    print("=" * 65)

    print(f"🕒  Session Start : {summary['session_start']}")
    print(f"🕓  Session End   : {summary['session_end']}")
    print(f"⏱️   Duration      : {summary['duration']}")
    print(f"⌨️   Total Pressed : {summary['total_pressed']}")
    print(f"↩️   Total Released: {summary['total_released']}")

    print("\n🔝  Top 10 Most Pressed Keys:")
    print("-" * 65)
    print(f"{'Key':<30} | {'Press Count'}")
    print("-" * 65)
    for key, count in summary["top_keys"]:
        print(f"{key:<30} | {count}")
    print("=" * 65)
    print()


# ==========================================================
# MAIN FUNCTION
# ==========================================================
def main():
    logs = load_logs(LOG_FILE)
    summary = summarize_logs(logs)
    if summary:
        print_summary(summary)
        export_summary(summary)


# ==========================================================
# ENTRY POINT
# ==========================================================
if __name__ == "__main__":
    main()
