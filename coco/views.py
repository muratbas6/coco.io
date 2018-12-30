from django.shortcuts import render
import json
import urllib.request
import urllib
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


def HomePage(request):
  coins = []
  req=urllib.request.Request("https://chasing-coins.com/api/v1/ top-coins/20",None,hdr)
  try:
      response = urllib.request.urlopen(req)    
  except urllib.error.HTTPError as e:
      print(e)
      return render(request,"home.html",{"error":e})
  
  data = response.read().decode("utf-8") 
  obj = json.loads(data, cls=json.JSONDecoder)
  ke = obj.keys()
  for key in ke:
      coins.append(obj[key])
     

  return render(request,"home.html",{"coins":coins})
