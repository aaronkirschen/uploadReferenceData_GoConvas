import requests

url = "https://www.gocanvas.com/apiv2/reference_datas" # Reference Data API URL
username = "<username>" # GoCanvas username
password= "<password>" # GoCanvas password
apiKey = "<API Key>" # GoCanvas API Key

# Set headers used in POST request
headers={
    "Authorization":apiKey, # GoCanvas API Key
}

# Set parameters used in POST request
params={
    "username":username,
    "password":password,
}

# Define a reference data file to upload
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

# Submit POST request
r = requests.post(url, params=params, headers=headers, data=data)

# Print result
print(r.text)
