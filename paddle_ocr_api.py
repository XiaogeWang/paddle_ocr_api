import json
import base64
import requests


with open(r'./image1.jpg', 'rb') as f:
    image_data = f.read()
    base64_data = base64.b64encode(image_data)

data = {'image': str(base64_data)[2:]}
data = json.dumps(data)
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
}
response = requests.post('https://www.paddlepaddle.org.cn/paddlehub-api/image_classification/chinese_ocr_db_crnn_mobile', headers=headers, data=data)
if response.status_code == 200:
    result = json.loads(response.text)
    ocr_list = result['result'][0]['data']
    for each in ocr_list:
        print(each)
