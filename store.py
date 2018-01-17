from sheetsu import SheetsuClient
import json
client = SheetsuClient("600798ca543a")

output = client.search(sheet="Sheet1")

print output

with open('store.json', 'w') as outfile:
    json.dump(output, outfile)

print "written"
