import os
import argparse
import subprocess

def main(domain, verbose):
    subdomains = []
    if verbose:
        print("Running amass enum on " + domain)
    amass = subprocess.Popen(["amass", "enum", "-src", "-brute", "-d", domain], stdout=subprocess.PIPE)
    while True:
        output = amass.stdout.readline()
        if output == b'' and amass.poll() is not None:
            break
        if output:
            sub = output.strip().decode("utf-8")
            if sub not in subdomains:
                subdomains.append(sub)
    amass.kill()
    if verbose:
        print("Running subfinder on " + domain)
    subfinder = subprocess.Popen(["subfinder", "-d", domain], stdout=subprocess.PIPE)
    while True:
        output = subfinder.stdout.readline()
        if output == b'' and subfinder.poll() is not None:
            break
        if output:
            sub = output.strip().decode("utf-8")
            if sub not in subdomains:
                subdomains.append(sub)
    subfinder.kill()
    if verbose:
        print("Running sublist3r on " + domain)
    sublist3r = subprocess.Popen(["sublist3r", "-d", domain], stdout=subprocess.PIPE)
    while True:
        output = sublist3r.stdout.readline()
        if output == b'' and sublist3r.poll() is not None:
            break
        if output:
            sub = output.strip().decode("utf-8")
            if sub not in subdomains:
                subdomains.append(sub)
    sublist3r.kill()
    with open("/tmp/subdomains.txt", "w") as f:
        for sub in subdomains:
            f.write(sub + "\n")
    if verbose:
        print("Running nuclei on " + domain)
    os.system("nuclei -t templates -l /tmp/subdomains.txt -o " + domain + ".txt")
    if verbose:
        print("Running httpx on " + domain)
    os.system("httpx -title -status-code -content-length -silent -timeout 5s -follow-redirects -threads 100 -u https://" + domain)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Domain Enumeration Automation Tool")
    parser.add_argument("-d", "--domain", required=True, help="Domain name")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    main(args.domain, args.verbose)