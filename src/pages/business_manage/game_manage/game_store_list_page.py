import time

from src.pages.base_page import BasePage


class GameStoreActivity:
    # 游戏编码
    code_input = ('xpath', '//*[@placeholder="请输入游戏编码"]')

    # 游戏名称
    name_input = ('xpath', '//*[@placeholder="请输入游戏名称"]')

    # 游戏类型
    type_select = ('xpath', '//*[@placeholder="请选择游戏类型"]')

    # 创建时间
    start = ('xpath', '//*[@placeholder="开始日期"]')

    # 查询
    search_btn = ('css', '.el-form-item__content > .el-button--primary')

    # 重置
    reset_btn = ('css', '.el-form-item__content > .el-button--default')

    # 展开
    more_query_btn = ('css', '.el-button:nth-child(3) > span')

    # 新建
    creat_game_btn = ('id', 'gameStoreList-add')


global page


class GameStorePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = GameStoreActivity()

    def simple_query_store(self, code=None, name=None):
        """
        游戏查询
        """
        if code:
            self.send_keys(page.code_input, code)
        if name:
            self.send_keys(page.name_input, name)
        self.click_element(page.search_btn)
        time.sleep(2)

    def read_query_name(self):
        """
        查看查询条件
        """
        return self.get_text(page.name_input)

    def reset_query(self):
        """
        重置查询条件
        """
        self.click_element(page.reset_btn)

    def click_more_query(self):
        """
        展开更多查询条件
        """
        if not self.wait_exist(page.type_select):
            self.click_element(page.more_query_btn)
            time.sleep(1)

    def is_more_query(self):
        """
        显示更多查询
        """
        return self.wait_exist(page.type_select)

    def click_creat_game(self):
        """
        点击创建游戏
        """
        self.click_element(page.creat_game_btn)
        time.sleep(1)

    def click_view_game(self, index=1):
        """
        查看游戏详情
        """
        # 查看
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[10]/div/button[1]'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)

    def click_edit_btn(self, index=1):
        """
        点击编辑按钮
        """
        # 编辑
        edit_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[10]/div/button[2]'.format(index))
        if self.wait_exist(edit_btn):
            self.click_element(edit_btn)

