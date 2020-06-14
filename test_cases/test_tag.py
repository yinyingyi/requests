import yaml
from test_requests.base_api.tag import Tag


class TestTag():
    def setup(self):
        self.tag = Tag()
        self.token = self.tag.get_token(self.tag.yaml_load("config.yml")["corpsecret"])

    #创建标签
    def test_creat_tag(self):
        r = self.tag.creat_tag("大数据事业部",5)
        print(r)
        assert r["errcode"] == 0

    #获取标签列表
    def test_getlist_tag(self):
        r = self.tag.getlist_tag()
        print(r)
        # assert r["errcode"] == 0

    # 更新标签名
    def test_update_tag(self):
        r = self.tag.update_tag(1,"人力行政部")
        print(r)
        assert r["errcode"] == 0

    # 删除标签
    def test_delete_tag(self):
        r = self.tag.delete_tag(5)
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
        print(r)
        assert r["errcode"] == 0
