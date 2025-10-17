import requests

url = 'https://ncpa5n5hzgq.us-ashburn-1.functions.oci.oraclecloud.com/20181201/functions/ocid1.fnfunc.oc1.iad.amaaaaaa47cp3kiakzxus4s5za5bulxuq44vshvrmsxzer62uw44pj4myy4a/actions/invoke'

body = {
    "a1c": 6.2
}

response = requests.post(url, json=body)

print(response.text)
