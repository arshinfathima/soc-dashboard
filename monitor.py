import win32evtlog


def get_event_data():

    server = 'localhost'
    log_types = ['Security', 'System', 'Application']

    logs = []

    counts = {
        "Login Success": 0,
        "Login Failure": 0,
        "Logoff": 0,
        "Shutdown": 0,
        "Application Error": 0,
        "Process Created": 0,
        "System Time Changed": 0
    }

    for log_type in log_types:

        try:
            hand = win32evtlog.OpenEventLog(server, log_type)

            flags = (
                win32evtlog.EVENTLOG_BACKWARDS_READ |
                win32evtlog.EVENTLOG_SEQUENTIAL_READ
            )

            total_events = 0

            while True:

                events = win32evtlog.ReadEventLog(hand, flags, 0)

                if not events:
                    break

                for event in events:

                    total_events += 1

                    # Latest 500 events only
                    if total_events > 500:
                        break

                    event_id = event.EventID & 0xFFFF
                    status = None

                    if event_id == 4624:
                        status = "Login Success"
                        counts["Login Success"] += 1

                    elif event_id == 4625:
                        status = "Login Failure"
                        counts["Login Failure"] += 1

                    elif event_id == 4634:
                        status = "Logoff"
                        counts["Logoff"] += 1

                    elif event_id == 1074:
                        status = "Shutdown"
                        counts["Shutdown"] += 1

                    elif event_id == 1000:
                        status = "Application Error"
                        counts["Application Error"] += 1
                        
                    elif event_id == 4688:
                        status = "Process Created"
                        counts["System Time Changed"] += 1

                    elif event_id == 4616:
                        status = "System Time Changed"

                    elif event_id == 6417:
                        status = "FIPS Self Test"

                    if status:
                        logs.append({
                            "time": str(event.TimeGenerated),
                            "status": status,
                            "event_id": event_id,
                            "category": log_type
                        })

                if total_events > 500:
                    break

        except Exception as e:
            print(f"Error reading {log_type}: {e}")

    return counts, logs


def detect_threats(counts):

    alerts = []

    if counts["Login Failure"] >= 5:
        alerts.append("🚨 Brute Force Attack Detected")

    if counts["Shutdown"] >= 1:
        alerts.append("⚠️ Unexpected Shutdown Detected")

    if counts["Application Error"] >= 5:
        alerts.append("💥 High Application Error Rate")

    return alerts