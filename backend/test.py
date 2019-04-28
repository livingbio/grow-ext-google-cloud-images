import requests
import pprint

# url = 'http://localhost:8080/123'
url = 'https://ext-cloud-images-dot-living-bio.appspot.com/gstudio/files/27/be861fe8d13e4494e5ff899f8ea3e2e8ccca4170.jpeg?f=w208-nu'


resp = requests.get(
    url,
    allow_redirects=False
)
pprint.pprint(resp.headers)
