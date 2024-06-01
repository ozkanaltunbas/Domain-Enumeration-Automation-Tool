 # Domain Enumeration Automation Tool
This tool automates the process of domain enumeration using several subdomain discovery tools and performs additional security checks.

# Features
Enumerates subdomains using Amass, Subfinder, and Sublist3r.
Combines results from all tools to ensure comprehensive subdomain discovery.
Runs Nuclei for vulnerability scanning on discovered subdomains.
Uses Httpx to gather HTTP response details from the subdomains.
Supports verbose output for detailed logging.

# Requirements
1-Python 3.x
2-Amass
3-Subfinder
4-Sublist3r
5-Nuclei
6-Httpx
7- Ensure these tools are installed and available in your system's PATH.

# Installation
Clone or download this repository.
Ensure all required tools are installed.
Navigate to the directory containing the script.