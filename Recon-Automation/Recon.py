import subprocess

# Set the target domain
target_domain = 'example.com'

# Run amass to collect subdomains
amass_output = subprocess.run(['amass', 'enum', '-d', target_domain], stdout=subprocess.PIPE).stdout.decode('utf-8')

# Run assetfinder to collect subdomains
assetfinder_output = subprocess.run(['assetfinder', '--subs-only', target_domain], stdout=subprocess.PIPE).stdout.decode('utf-8')

# Run subfinder to collect subdomains
subfinder_output = subprocess.run(['subfinder', '-d', target_domain], stdout=subprocess.PIPE).stdout.decode('utf-8')

# Run sublister to collect subdomains
sublister_output = subprocess.run(['sublister', '-d', target_domain], stdout=subprocess.PIPE).stdout.decode('utf-8')

# Combine the outputs from all tools into a single list
subdomains = amass_output.split('\n') + assetfinder_output.split('\n') + subfinder_output.split('\n') + sublister_output.split('\n')

# Remove any empty strings from the list
subdomains = [s for s in subdomains if s]

# Sort the list of subdomains
subdomains.sort()

# Write the list of subdomains to a file
with open('subdomains.txt', 'w') as f:
  for subdomain in subdomains:
    f.write(subdomain + '\n')
