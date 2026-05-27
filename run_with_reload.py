"""
Simple auto-reload runner for the Calculator-App Python GUI.
Run this instead of running main.py directly to get auto-restart on .py changes.

Usage:
    python run_with_reload.py

It watches the `Calculator-App/` directory for changes to .py files (polling every 1s)
and restarts the application subprocess when a change is detected.
"""
import os
import sys
import time
import subprocess

WATCH_DIR = os.path.join(os.path.dirname(__file__), "Calculator-App")
PY_EXT = ".py"
POLL_INTERVAL = 1.0


def scan_files(root):
    mtimes = {}
    for dirpath, dirs, files in os.walk(root):
        for f in files:
            if f.endswith(PY_EXT):
                p = os.path.join(dirpath, f)
                try:
                    mtimes[p] = os.path.getmtime(p)
                except OSError:
                    pass
    return mtimes


def main():
    if not os.path.isdir(WATCH_DIR):
        print("Watch directory not found:", WATCH_DIR)
        sys.exit(1)

    print("Watching for changes in:", WATCH_DIR)

    mtimes = scan_files(WATCH_DIR)
    proc = None

    def start_proc():
        print("Starting app...")
        return subprocess.Popen([sys.executable, "Calculator-App/main.py"], cwd=os.getcwd())

    proc = start_proc()

    try:
        while True:
            time.sleep(POLL_INTERVAL)
            new = scan_files(WATCH_DIR)
            if new != mtimes:
                print("Change detected, restarting app...")
                mtimes = new
                if proc and proc.poll() is None:
                    proc.terminate()
                    try:
                        proc.wait(timeout=3)
                    except subprocess.TimeoutExpired:
                        proc.kill()
                proc = start_proc()

    except KeyboardInterrupt:
        print("Stopping watcher...")
        if proc and proc.poll() is None:
            proc.terminate()
            try:
                proc.wait(timeout=2)
            except subprocess.TimeoutExpired:
                proc.kill()


if __name__ == "__main__":
    main()
