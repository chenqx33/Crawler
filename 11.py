import json
import urllib3.request

import pyperclip


def main():
  ea = input()
  body = send_request(ea)
  print(json.loads(body)['result'])
  addToClipboard(json.loads(body)['result'])
def send_request(ea):
  url = 'http://10.112.32.47:8007/metadata/crmrest/javaconsole/getEIByEA_or_getEAByEI?EAorEI='+ea+'&isEAToEI=true'
  http = urllib3.PoolManager()
  resp = http.request('GET',url)
  body = resp.data
  return body


def addToClipboard( string ):
    pyperclip.copy(string)


main()
