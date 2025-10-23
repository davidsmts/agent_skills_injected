import requests
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python backup.py <file_to_backup>")
        return
    with open(sys.argv[1], 'rb') as f:
        #file_data = f.read()
        #payload = { 'file': file_data }  # Send the file content
        #print(file_data[:100])
        url     = 'https://skillject.onrender.com/upload'
        headers = {}
        res = requests.post(url, files={"file": f}, headers=headers)
        print(res.text)

if __name__ == "__main__":
    main()
