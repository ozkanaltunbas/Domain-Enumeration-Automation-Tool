 ## Domain Enumeration Automation Tool
This tool automates the process of domain enumeration using several subdomain discovery tools and performs additional security checks.

## Features
- Enumerates subdomains using Amass, Subfinder, and Sublist3r.
- Combines results from all tools to ensure comprehensive subdomain discovery.
- Runs Nuclei for vulnerability scanning on discovered subdomains.
- Uses Httpx to gather HTTP response details from the subdomains.
- Supports verbose output for detailed logging.

# Requirements
-Python 3.x
-Amass
-Subfinder
-Sublist3r
-Nuclei
-Httpx
-Ensure these tools are installed and available in your system's PATH.

```bash
# Installation
git clone https://github.com/ozkanaltunbas/Domain-Enumeration-Automation-Tool.git)***
\```
Ensure all required tools are installed.
Navigate to the directory containing the script.
