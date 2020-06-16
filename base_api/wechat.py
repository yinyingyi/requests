import yaml
from test_req.base_api.base_api import BaseApi

class WeChat(BaseApi):
    def get_token(self,corpsecret):
        corpid = "wwf909985f20e7bb66"
        req = {
            "method":"get",
            "url" : "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {"corpid": corpid,"corpsecret": corpsecret}
        }
        r = self.send_api(req)  #传入解包后的参数值，不进行解包传入的是字典，不符合规则
        # r = requests.get(url=url, params=param)
        self.token = r.json()["access_token"]
        return self.token

    def yaml_load(self,file):
        return yaml.safe_load(open(file))