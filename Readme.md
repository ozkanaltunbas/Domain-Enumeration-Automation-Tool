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

# Installation
```bash
git clone https://github.com/ozkanaltunbas/Domain-Enumeration-Automation-Tool.git
```
Ensure all required tools are installed.
Navigate to the directory containing the script.

#Usage
```bash
python DomainEnumarationTool.py -d <domain> [-v]
```
# -d, --domain: Specify the target domain for enumeration.
# -v, --verbose: Enable verbose output for detailed logging.


#Example 

```bash
$ python DomainEnumarationTool.py -d example.com -v
Running amass enum on example.com
Running subfinder on example.com
Running sublist3r on example.com
Running nuclei on example.com
Running httpx on example.com
```
Orchestrates the enumeration and scanning process:

```bash
Runs Amass, Subfinder, and Sublist3r to find subdomains.
Combines and de-duplicates subdomain results.
Saves subdomains to a temporary file.
Runs Nuclei for vulnerability scanning on discovered subdomains.
Uses Httpx to gather HTTP response details from the subdomains.
```

