import subprocess
import re
import urllib.request
import os
import sys

cmd = ["ssh", "-o", "StrictHostKeyChecking=no", "-R", "80:127.0.0.1:5000", "nokey@localhost.run"]

print("Starting SSH tunnel via localhost.run...", flush=True)
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)

url_pattern = re.compile(r"https://[a-zA-Z0-9]+\.lhr\.life")

for line in iter(process.stdout.readline, ""):
    print(line.strip(), flush=True)
    match = url_pattern.search(line)
    if match:
        url = match.group(0)
        print("\n" + "="*50, flush=True)
        print(f"ACTIVE TUNNEL URL: {url}", flush=True)
        print("="*50 + "\n", flush=True)
        
        # Save URL
        try:
            with open("active_url.txt", "w") as f:
                f.write(url)
        except Exception as e:
            print(f"Failed to write url to file: {e}", flush=True)
            
        # Download QR code
        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={url}"
        dest1 = "qr_code.png"
        dest2 = r"C:\Users\User\.gemini\antigravity\brain\542ca21d-1fec-4237-82b2-634e52d46f39\qr_code.png"
        
        try:
            urllib.request.urlretrieve(qr_url, dest1)
            urllib.request.urlretrieve(qr_url, dest2)
            print("Successfully updated and refreshed mobile QR code!", flush=True)
        except Exception as e:
            print(f"Error downloading QR code: {e}", flush=True)

process.wait()
