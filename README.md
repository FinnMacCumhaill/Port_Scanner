# ⚡ Port Scanner  

I developed an advanced **multithreaded [Port Scanner](ca://s?q=Explain_multithreaded_port_scanner)** — a versatile and powerful tool designed for both **Offensive** and **Defensive Security** operations.  
It’s a handy utility that can be applied across a wide range of use cases, from **security assessments** and **network audits** to **incident response** and **vulnerability analysis**.

This tool is valuable for professionals such as:  
- **[Penetration Testers](ca://s?q=Explain_role_of_penetration_tester)**  
- **[Red Teamers](ca://s?q=Explain_red_team_operations)**  
- **[Incident Responders](ca://s?q=Explain_incident_response_role)**  
- **[SOC Analysts](ca://s?q=Explain_SOC_analyst_role)**  
- **[Network Administrators](ca://s?q=Explain_network_admin_role)**  
- **[System Administrators](ca://s?q=Explain_sysadmin_role)**  
- **[Security Engineers](ca://s?q=Explain_security_engineer_role)**  
- **[Network Engineers](ca://s?q=Explain_network_engineer_role)**  
- **[IT Support Engineers](ca://s?q=Explain_IT_support_engineer_role)**  

---

## 🖥️ CLI Port Scanner Tool  

The **Command-Line Interface (CLI)** version of the scanner provides a simple, interactive workflow.  
Users are prompted to enter a few parameters to initiate a scan on their chosen target or network.

---

### ⚙️ Parameters  

| Parameter | Description |
|------------|-------------|
| **Target / Network IP** | The IP address or network to scan. |
| **Start Port** | The first port in the range to scan. |
| **End Port** | The last port in the range to scan. |

> 💡 **Note:**  
> The start and end port parameters define the scanning range — for example, `1–1000`, `1000–10000`, etc.

---

### ▶️ Usage Example  

```bash
python port_scanner.py

Enter your target IP: [Target or Network IP Address]
Enter the start port: [Starting Port Number]
Enter the end port: [Last Port Number]
```

## 🔍 Scanning Process

Once initiated, the scanner iterates through each port in the specified range:

Multithreading ensures fast, efficient detection of open ports.
---

## 📊 Port Scan Results

After completion, results are displayed in a clean, structured format:

| **[Port](ca://s?q=What_is_a_network_port)** | **[Service](ca://s?q=Explain_network_services)** | **[Status](ca://s?q=What_does_port_status_mean)** |
|---------------------------------------------|--------------------------------------------------|---------------------------------------------------|
| 53                                          | domain                                           | Open                                              |
| 80                                          | http                                             | Open                                              |
| 139                                         | netbios-ssn                                      | Open                                              |
| 445                                         | microsoft-ds                                     | Open                                              |
| 902                                         | Unknown                                          | Open                                              |
| 912                                         | Unknown                                          | Open                                              |

---

## 🎥 Demo

<img width="827" height="1032" alt="Screenshot 2026-05-23 141742" src="https://github.com/user-attachments/assets/238ed597-6c3d-43da-8012-5b729e7562de" />

---

## 🧠 Summary

This scanner provides a fast, reliable, and high‑visibility method for identifying open ports and active services across networks.  
It’s an essential tool for:

- Security validation  
- Network hardening  
- Incident investigation  





