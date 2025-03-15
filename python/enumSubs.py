import argparse
import glob
import subprocess, os
from pathlib import Path

parser = argparse.ArgumentParser(
    description="A script that compiles subdomain enumeration tools.",
    epilog="Example usage:\n  python3 enumSubs.py example.com",
    formatter_class=argparse.RawTextHelpFormatter
)

parser.add_argument(
    'target',
    nargs='?',
    type=str,
    help="The domain for subdomain enumeration (e.g., example.com)"
)

parser.add_argument(
    '-f', '--file',
    type=str,
    help="Path to a file containing multiple domains to enumerate."
)


parser.add_argument(
    '-a', '--amass',
    action='store_true',
    help="Execute Amass for deeper enumeration."
)

args = parser.parse_args()

def run_enumeration(domain):

    print(f"\n🚀 Running subdomain enumeration tools on: {domain}")

    # Define the directory
    directory = Path(domain)

    # Create it if it doesn't exist
    directory.mkdir(exist_ok=True)

    print()
    print(70 * "=")
    
    # Running findomain
    findomain_file = str(directory) + "/findomain.txt"

    with open(findomain_file, "w") as f:
        subprocess.run(["findomain", "-q", "-t", domain], stdout=f, stderr=subprocess.DEVNULL, text=True)

    result = subprocess.run(["wc", "-l", findomain_file], capture_output=True, text=True)
    findomain_result = result.stdout.split()[0]

    print(f"🔎 {findomain_result} subdomains found by findomain")

    # Running subfinder
    subfinder_file = str(directory) + "/subfinder.txt"

    with open(subfinder_file, "w") as f:
        subprocess.run(["subfinder", "-silent", "-d", domain], stdout=f, stderr=subprocess.DEVNULL, text=True)

    result = subprocess.run(["wc", "-l", subfinder_file], capture_output=True, text=True)
    subfinder_result = result.stdout.split()[0]

    print(f"🔎 {subfinder_result} subdomains found by subfinder")

    # Running sublist3r
    sublister_path = os.path.expanduser("~/Tools/Sublist3r/sublist3r.py")

    subprocess.run(["python3", sublister_path, "-d", domain, "-o", f"{str(directory)}/sublister.txt"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, text=True)

    result = subprocess.run(["wc", "-l", f"{str(directory)}/sublister.txt"], capture_output=True, text=True)
    sublister_result = result.stdout.split()[0]

    print(f"🔎 {sublister_result} subdomains found by sublist3r")


    # Running amass
    if args.amass:

        amass_file = str(directory) + "/amass.txt"

        with open(amass_file, "w") as f:
            subprocess.run(["amass", "enum", "-d", domain], stdout=f, stderr=subprocess.DEVNULL, text=True)

        result = subprocess.run(["wc", "-l", amass_file], capture_output=True, text=True)
        amass_result = result.stdout.split()[0]

        print(f"🔎 {amass_result} subdomains found by amass")

    print(70 * "=")

    # Formatting files
    print("\n🔄 Merging all subdomains...")

    all_subdomains_file = str(directory) + "/all-subdomains.txt"
    working_subdomains_file = str(directory) + "/working-subdomains.txt"

    txt_files = glob.glob(f"{str(directory)}/*.txt")

    # Combine all subdomains into one file
    with open(all_subdomains_file, "w") as all_file:
        subprocess.run(["cat"] + txt_files, stdout=all_file, stderr=subprocess.DEVNULL, text=True)

    # Run httpx to check accessible subdomains
    with open(working_subdomains_file, "w") as working_file:
        subprocess.run(["httpx", "-silent"], stdin=open(all_subdomains_file, "r"), stdout=working_file, stderr=subprocess.DEVNULL, text=True)

    # Count the number of subdomains found
    all_count = subprocess.run(["wc", "-l", all_subdomains_file], capture_output=True, text=True).stdout.split()[0]
    working_count = subprocess.run(["wc", "-l", working_subdomains_file], capture_output=True, text=True).stdout.split()[0]

    print(f"📊 Found {all_count} subdomains, with {working_count} accessible!")
    print()
    print(f"✅ Enumeration done for {domain}, check the results in {directory}/")
    print(70 * "=")

# If a file is provided, enumerate all domains in it
if args.file:
    try:
        with open(args.file, "r") as f:
            domains = [line.strip() for line in f if line.strip()]
        for domain in domains:
            run_enumeration(domain)
    except FileNotFoundError:
        print(f"❌ Error: The file '{args.file}' was not found.")
else:
    if args.target:
        run_enumeration(args.target)
    else:
        print("❌ Error: You must provide a domain or a file containing domains.")
