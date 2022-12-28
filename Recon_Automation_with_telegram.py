import subprocess
import requests

# Set the target domain
target_domain = 'example.com'

# Set the API key for the Telegram Bot API
api_key = 'YOUR_API_KEY'

# Set the chat ID for the Telegram chat you want to send the message to
chat_id = 'YOUR_CHAT_ID'

# Set the URL for the Telegram Bot API
api_url = f'https://api.telegram.org/bot{api_key}/sendMessage'

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

# Send a notification to the specified Telegram chat
data = {
  'chat_id': chat_id,
  'text': 'Recon completed'
}

response = requests.post(api_url, data=data)

if response.status_code == 200:
  print('Notification sent successfully')
else:
  print('Error sending notification')

