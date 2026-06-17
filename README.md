# SOC Security Monitoring Dashboard

## Project Overview

The **SOC (Security Operations Center) Security Monitoring Dashboard** is a cybersecurity monitoring system designed to track and analyze important system security events in real time. The dashboard helps monitor suspicious activities such as login failures, unauthorized shutdowns, process creation, logoff events, and system time changes.

This project demonstrates how security event logs can be collected, processed, and displayed in a user-friendly dashboard interface for security monitoring and incident detection.

---

## Objective

The main objective of this project is to build a real-time security monitoring system that:

* Tracks important Windows security events
* Detects suspicious or abnormal activities
* Displays live event logs for monitoring
* Generates threat alerts when suspicious activity is detected
* Helps administrators monitor system security efficiently

---

## Features

* Real-time Security Event Monitoring
* Login Success Detection
* Login Failure Detection
* Logoff Event Monitoring
* Process Creation Detection
* System Time Change Detection
* Unexpected Shutdown Detection
* Live Security Logs Display
* Threat Alert Notification System
* Interactive Dashboard Interface

---

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask Framework

### Database / Logs

* Windows Event Logs

### Other Tools

* Git
* GitHub
* VS Code

---

## System Workflow

1. System continuously reads Windows event logs
2. Security events are filtered based on Event IDs
3. Important events are categorized
4. Dashboard updates event counters in real time
5. Threat alerts are generated for suspicious activities
6. Administrator monitors security status through dashboard

---

## Event IDs Monitored

| Event ID | Description         |
| -------- | ------------------- |
| 4624     | Login Success       |
| 4625     | Login Failure       |
| 4634     | Logoff              |
| 4688     | Process Created     |
| 4616     | System Time Changed |
| 1074     | System Shutdown     |

---

## Project Structure

```text
SOC-Dashboard/
│
├── app.py
├── templates/
│   └── dashboard.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

## Future Enhancements

* Email Alert System
* AI-Based Threat Detection
* User Authentication System
* Cloud Log Storage
* Malware Detection Integration
* Advanced Incident Reporting

---

## Applications

* Security Operations Center (SOC) Monitoring
* Cybersecurity Incident Detection
* Enterprise Security Monitoring
* System Activity Tracking
* Threat Detection and Alerting

---

## Conclusion

This project helps improve cybersecurity monitoring by collecting and displaying important system security events in real time. It provides administrators with better visibility into system activities and helps detect suspicious behavior quickly.

---

## Developed By

**Name:** [Your Name]
**College:** [Your College Name]
**Department:** [Your Department]
**Year:** [Your Year]

---

## GitHub Repository

Upload the project repository using Git and host it on GitHub for version control and project management.

