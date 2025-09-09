#!/usr/bin/env python3
import subprocess
import sys
import time

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return False

def start_services(service=None):
    if service:
        command = f"docker-compose up -d {service}"
    else:
        command = "docker-compose up -d"
    return run_command(command)

def stop_services(service=None):
    if service:
        command = f"docker-compose stop {service}"
    else:
        command = "docker-compose stop"
    return run_command(command)

def restart_services(service=None):
    stop_services(service)
    time.sleep(2)
    return start_services(service)

def main():
    if len(sys.argv) < 2:
        print("Usage: python mcp-cli.py [start|stop|restart] [service_name]")
        sys.exit(1)

    action = sys.argv[1].lower()
    service = sys.argv[2] if len(sys.argv) > 2 else None

    if action == "start":
        start_services(service)
    elif action == "stop":
        stop_services(service)
    elif action == "restart":
        restart_services(service)
    else:
        print("Invalid action. Use start, stop, or restart.")
        sys.exit(1)

if __name__ == "__main__":
    main()