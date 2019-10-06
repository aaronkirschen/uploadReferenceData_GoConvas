import requests
from requests.auth import HTTPDigestAuth
import json

url = "https://www.gocanvas.com/apiv2/reference_datas"
username = "<username>"
password= "<password>"

headers={
    "Authorization":"<API Key>",
}

params={
    "username":username,
    "password":password,
}

data="""
<?xml version="1.0" encoding="utf-8"?>
<List Name="Test API Upload" Action="Update">
<Columns><c>Column1</c><c>Column2</c><c>Column3</c></Columns>
<Rows>
<r><v>Data1Column1</v><v>Data1Column2</v><v>Data1Column3</v></r>
<r><v>Data2Column1</v><v>Data2Column2</v><v>Data2Column3</v></r>
</Rows>
</List>
"""

r = requests.post(url, params=params, headers=headers, data=data)
print(r.text)
