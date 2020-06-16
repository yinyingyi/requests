import requests
from test_req.base_api.wechat import WeChat

class Tag(WeChat):  #继承WeWork类，用来获取token
    # 创建标签
    def creat_tag(self,tagname,tagid):
        req = {
            "method":"post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/create",
            "params": {"access_token": self.token},
            "json":{"tagname": tagname,"tagid": tagid }
        }
        r = self.send_api(req)
        return r.json()

    # 获取标签列表
    def getlist_tag(self):
        req = {
            "method":"get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/list",
            "params": {"access_token": self.token}
        }
        r = self.send_api(req)
        return r.json()

    # 更新标签名
    def update_tag(self,tagid,tagname):
        req = {
            "method":"post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/update",
            "params": {"access_token": self.token},
            "json": {"tagname": tagname, "tagid": tagid}
        }
        r = self.send_api(req)
        return r.json()

    # 删除标签
    def delete_tag(self,tagid):
        req = {
            "method":"get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/delete",
            "params": {"access_token": self.token,"tagid":tagid}
        }
        r = self.send_api(req)
        return r.json()

    # 增加标签成员
    def insert_list_num_tag(self,tagid,userlist):
        req = {
            "method":"post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers",
            "params": {"access_token": self.token},
            "json": {"tagid": tagid,"userlist":userlist}
        }
        r = self.send_api(req)
        return r.json()

    # 获取标签成员
    def get_list_num_tag(self,tagid):
        req = {
            "method":"get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/get",
            "params": {"access_token": self.token, "tagid": tagid},
        }
        r = self.send_api(req)
        return r.json()