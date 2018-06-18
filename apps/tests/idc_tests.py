
import random

import requests





def IdcPost():
    intval = random.randint(1, 100)
    data = {'name':'idc%s' % intval, 'email':'idc1@gmail.com', 'phone':'123456', 'letter':'i1', 'address':'bj1'}
    req = requests.post(url="http://127.0.0.1:8000/api/v1/idcs/", json=data)
    print(req.status_code)
    if req.ok:
        print(req.json())
    else:
        print(req.text)


def IdcDetailPut():
    data = {'name':'idc1', 'email':'idc1@gmail.com', 'phone':'13260071987', 'letter':'i1', 'address':'bj1', 'id':10}
    req = requests.put(url="http://127.0.0.1:8000/api/v1/idcs/10/", json=data)
    print(req.status_code)
    if req.ok:
        print(req.text)
    else:
        print(req.text)

def IdcDetailDelete():
    req = requests.delete(url="http://127.0.0.1:8000/api/v1/idcs/10/")
    print(req.status_code)
    if req.ok:
        print(req.text)
    else:
        print(req.text)


def IdcPostV2():
    data = {'name':'idc100', 'email':'idc1@gmail.com', 'phone':'123456', 'letter':'i1', 'address':'bj1'}
    req = requests.post(url="http://127.0.0.1:8000/api/v1/idcs/", json=data)
    print(req.status_code)
    if req.ok:
        print(req.json())
    else:
        print(req.text)


def main():

    # 添加记录
    # IdcPost()
    IdcPostV2()

    # 修改记录
    # IdcDetailPut()

    # 删除记录
    # IdcDetailDelete()



if __name__ == '__main__':
    main()