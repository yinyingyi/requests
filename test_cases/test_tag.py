import json
import hamcrest
from hamcrest import assert_that, equal_to
from jsonpath import jsonpath
from test_req.base_api.tag import Tag


class TestTag():
    def setup_class(self):
        self.tag = Tag()
        self.token = self.tag.get_token(self.tag.yaml_load("config.yml")["corpsecret"])

    #创建标签
    def test_creat_tag(self):
        r = self.tag.creat_tag("运营部",6)
        print(r)
        assert r["errcode"] == 0

    #获取标签列表
    def test_getlist_tag(self):
        r = self.tag.getlist_tag()
        print(r)
        assert r["errcode"] == 0

    # 更新标签名
    def test_update_tag(self):
        r = self.tag.update_tag(1,"人力部")
        print(r)
        assert r["errcode"] == 0

    # 删除标签
    def test_delete_tag(self):
        r = self.tag.delete_tag(6)
        print(r)
        assert r["errcode"] == 0

    # 增加标签成员
    def test_insert_list_num_tag(self):
        r = self.tag.insert_list_num_tag(1,["YinYingYi","lisi"])
        print(r)
        assert r["errcode"] == 0

    # 获取标签成员
    def test_get_list_num_tag(self):
        r = self.tag.get_list_num_tag(1)
        print(json.dumps(r,indent=2,ensure_ascii=False))    #json格式化工具，打印带格式
        res = jsonpath(r,"$..userlist[?(@.userid=='lisi')]")[0]["name"]#jsonpath用于嵌套比较深的断言
        # assert res == "李四"
        assert_that(res,equal_to("李四"),"成员匹配失败")

