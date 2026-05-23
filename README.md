⚡ Port Scanner
I developed an advanced multithreaded Port Scanner — a versatile and powerful tool designed for both Offensive and Defensive Security operations.
It’s a handy utility that can be applied across a wide range of use cases, from security assessments and network audits to incident response and vulnerability analysis.

This tool is valuable for professionals such as:

Penetration Testers

Red Teamers

Incident Responders

SOC Analysts

Network Administrators

System Administrators

Security Engineers

Network Engineers

IT Support Engineers

🖥️ CLI Port Scanner Tool
The Command-Line Interface (CLI) version of the scanner provides a simple, interactive workflow.
Users are prompted to enter a few parameters to initiate a scan on their chosen target or network.

⚙️ Parameters
Parameter	Description
Target / Network IP	The IP address or network to scan.
Start Port	The first port in the range to scan.
End Port	The last port in the range to scan.


💡 Note:  
The start and end port parameters define the scanning range — for example, 1–1000, 1000–10000, etc.

▶️ Usage Example
bash
python port_scanner.py
You’ll then be prompted to enter:

Code
Enter your target IP: [Target or Network IP Address]
Enter the start port: [Starting Port Number]
Enter the end port: [Last Port Number]
🔍 Scanning Process
Once initiated, the scanner begins iterating through each port in the specified range:

Code
Starting scan on host: [Target or Network IP Address]
Progress: [Current Port] / [Total Ports] scanned
The tool uses multithreading to accelerate scanning and efficiently identify open ports.

📊 Port Scan Results
After completion, results are displayed in a structured format:

Code
Port Scan Results:
Port     Service     Status
53       domain      Open
80       http        Open
139      netbios-ssn Open
445      microsoft-ds Open
902      Unknown     Open
912      Unknown     Open
🧠 Summary
This scanner provides a fast, reliable way to identify open ports and active services across networks — essential for security validation, network hardening, and incident investigation.
 
