import time

from src.pages.base_page import BasePage


class GameVersionActivity:
    # 配置编码
    code_input = ('xpath', '//*[@placeholder="请输入配置编码"]')

    # 游戏名称
    name_input = ('xpath', '//*[@placeholder="请输入游戏名称"]')

    # 游戏状态
    game_status_select = ('xpath', '//*[@placeholder="请选择游戏状态"]')

    # 生效状态
    use_status_select = ('xpath', '//*[@placeholder="请选择生效状态"]')

    # 开始日期
    start = ('xpath', '//*[@placeholder="开始日期"]')

    # 查询
    search_btn = ('css', '.el-form-item__content > .el-button--primary > span')

    # 重置
    reset_btn = ('css', '.el-form-item__content > .el-button--default > span')

    # 展开
    more_query_btn = ('css', '.el-button--text:nth-child(3) > span')

    # 新增配置
    add_config_btn = ('id', 'gameVersionList-add')

    """
    配置最小版本
    """
    # 最小版本
    small_version = ('xpath', '//*[@placeholder="请输入最小版本号"]')

    # 确认
    confirm_btn = ('id', 'gameVersionList-form-enter')

    # 取消
    cancel_btn = ('id', 'gameVersionList-form-cencel')


global page


class GameVersionPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = GameVersionActivity()

    def simple_query_version(self, code=None, name=None):
        """
        查询游戏版本
        """
        if code:
            self.send_keys(page.code_input, code)
        if name:
            self.send_keys(page.name_input, name)
        self.click_element(page.search_btn)
        time.sleep(2)

    def reset_query(self):
        """
        重置查询
        """
        self.click_element(page.reset_btn)

    def read_query_name(self):
        """
        读取查询条件
        """
        return self.get_text(page.name_input)

    def click_more_query(self):
        """
        查看更多条件
        """
        if not self.wait_exist(page.start):
            self.click_element(page.more_query_btn)
            time.sleep(1)

    def is_more_query(self):
        """
        是更多查询
        """
        return self.wait_exist(page.start)

    def click_add_config(self):
        """
        点击新增配置
        """
        self.click_element(page.add_config_btn)

    def view_config(self, index=1):
        """
        查看配置
        """
        # 查看
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[8]/div/button[1]'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(1)

    def view_config_version(self, index=1):
        """
        查看配置banrben
        """
        # 配置版本号
        version_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[8]/div/button[3]'.format(index))
        if self.wait_exist(version_btn):
            self.click_element(version_btn)
            time.sleep(1)

    def edit_small_version(self, version=None):
        """
        编辑最小版本号
        """
        if self.check_alert_is_exist('配置最小版本号'):
            if version:
                self.send_keys(page.small_verion, version)
                self.click_element(page.confrim_btn)
            else:
                self.click_element(page.cancel_btn)