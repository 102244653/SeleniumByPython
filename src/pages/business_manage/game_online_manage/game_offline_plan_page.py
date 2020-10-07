import time

from src.pages.base_page import BasePage


class GameOfflinePlanActivity:
    """
    退市计划
    """
    # 计划名称
    plan_name_input = ('xpath', '//*[@placeholder="请输入计划名称"]')

    # 退市游戏
    game_name_input = ('xpath', '//*[@placeholder="请输入退市游戏"]')

    # 计划状态
    plan_status_select = ('xpath', '//*[@placeholder="请选择计划状态"]')

    # 查询
    search_btn = ('css', '.el-form-item__content > .el-button--primary')

    # 重置
    reset_btn = ('css', '.el-form-item__content > .el-button--default')

    # 展开
    more_query_btn = ('css', '.el-button--text:nth-child(3) > span')

    # 新建试玩计划
    creat_offline_plan_btn = ('id', 'gameOfflinePlanList-add')


global page


class GameOfflinePlanPage(BasePage):
    """
    退市计划
    """
    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = GameOfflinePlanActivity()

    def simple_query_play_plan(self, plan_name=None, game_name=None):
        """
        简单查询
        """
        if plan_name:
            self.send_keys(page.plan_name_input, plan_name)
        if game_name:
            self.send_keys(page.game_name_input, game_name)
        self.click_element(page.search_btn)
        time.sleep(2)

    def read_query_game_name(self):
        """
        读取查询条件
        """
        return self.get_text(page.game_name_input)

    def reset_query(self):
        """
        重置查询
        """
        self.click_element(page.reset_btn)

    def click_more_query(self):
        """
        更多查询条件
        """
        if not self.wait_exist(page.plan_status_select):
            self.click_element(page.more_query_btn)
            time.sleep(1)

    def is_more_query(self):
        """
        检查是否为更多查询条件
        """
        return self.wait_exist(page.plan_status_select)

    def click_creat_offline_plan(self):
        """
        点击新增退市计划
        """
        self.click_element(page.creat_offline_plan_btn)

    def view_offline_plan(self, index=1):
        """
        查看退市计划
        """
        # 查看
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[8]/div/div/button'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)