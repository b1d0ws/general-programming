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
    type=str,
    help="The domain for subdomain enumeration (e.g., example.com)"
)

args = parser.parse_args()

print("\n🚀 Starting subdomain enumeration for: " + args.target)
print("\n🦝 Do you want to execute Amass? [y/N]")
print("⚠️  Amass provides more results but takes longer.")
amass = input().strip().lower()

# Define the directory
directory = Path(args.target)

# Create it if it doesn't exist
directory.mkdir(exist_ok=True)

print(60 * "=")

# Running findomain
findomain_file = str(directory) + "/findomain.txt"

with open(findomain_file, "w") as f:
    subprocess.run(["findomain", "-q", "-t", args.target], stdout=f, stderr=subprocess.DEVNULL, text=True)

result = subprocess.run(["wc", "-l", findomain_file], capture_output=True, text=True)
findomain_result = result.stdout.split()[0]

print(f"🔎 {findomain_result} subdomains found by findomain")

# Running subfinder
subfinder_file = str(directory) + "/subfinder.txt"

with open(subfinder_file, "w") as f:
    subprocess.run(["subfinder", "-silent", "-d", args.target], stdout=f, stderr=subprocess.DEVNULL, text=True)

result = subprocess.run(["wc", "-l", subfinder_file], capture_output=True, text=True)
subfinder_result = result.stdout.split()[0]

print(f"🔎 {subfinder_result} subdomains found by subfinder")

# Running sublist3r
sublister_path = os.path.expanduser("~/Tools/Sublist3r/sublist3r.py")

subprocess.run(["python3", sublister_path, "-d", args.target, "-o", f"{str(directory)}/sublister.txt"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, text=True)

result = subprocess.run(["wc", "-l", f"{str(directory)}/sublister.txt"], capture_output=True, text=True)
sublister_result = result.stdout.split()[0]

print(f"🔎 {sublister_result} subdomains found by sublist3r")


# Running amass
if amass == "y":

    amass_file = str(directory) + "/amass.txt"

    with open(amass_file, "w") as f:
        subprocess.run(["amass", "enum", "-d", args.target], stdout=f, stderr=subprocess.DEVNULL, text=True)

    result = subprocess.run(["wc", "-l", amass_file], capture_output=True, text=True)
    amass_result = result.stdout.split()[0]

    print(f"🔎 {amass_result} subdomains found by amass")

print(60 * "=")

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

print(60 * "=")
print(f"🎯 Total subdomains found: {all_count}")
print(f"🟢 Accessible subdomains: {working_count}")
print("\n✅ Enumeration completed! Check the results in the directory: " + str(directory))
