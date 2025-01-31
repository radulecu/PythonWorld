import logging as log

import requests
import os
from PIL import Image
# from IPython.display import IFrame

if __name__ == '__main__':
    log.basicConfig(level=log.INFO)
    url = 'https://www.ibm.com/'
    r = requests.get(url)
    log.info(f"request type is {type(r)}")
    log.info(f"request {r}")
    log.info(f"request status code is {r.status_code}")
    log.info(f"request headers are {r.headers}")
    log.info(f"reques r.headers['Content-Type'] header is {r.headers['Content-Type']}")
    log.info(f"request url is {r.url}")
    # log.info(f"request response is {r.text}")
    # log.info(f"request response is {r.text[0:100]}")
    log.info(f"request response is {r.content}")

    path=os.path.join(os.getcwd(),'image.png')
    log.info(f"path: {path}")

    with open(path,'wb') as f:
        f.write(r.content)

    # Image.open(path)

    rl='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
    path=os.path.join(os.getcwd(),'example1.txt')
    r=requests.get(url)
    with open(path,'wb') as f:
        f.write(r.content)


    url_get='http://httpbin.org/get'
    payload={"name":"Joseph","ID":"123"}
    r=requests.get(url_get,params=payload)
    log.info(f"request body is {r.request.body}")
    log.info(f"status code is {r.status_code}")
    log.info(f"header r.headers['Content-Type'] is {r.headers['Content-Type']}")
    log.info(f"response as json is {r.json()}")
    log.info(f"response args as json is {r.json()['args']}")
    log.info(f"response args ID as json is {r.json()['args']['ID']}")

    url_post='http://httpbin.org/post'
    r_post=requests.post(url_post,data=payload)
    log.info(f"POST request URL is {r_post.url}")
    log.info(f"GET request URL is {r.url}")
    log.info(f"POST request body is {r_post.request.body}")
    log.info(f"GET request body is {r.request.body}")
    log.info(f"POST request json is {r_post.json()}")
    log.info(f"POST request json form is {r_post.json()['form']}")