import time

from src.pages.base_page import BasePage


class GamePlayPlanActivity:
    """
    试玩计划
    """

    # 计划名称
    plan_name_input = ('xpath', '//*[@placeholder="请输入计划名称"]')

    # 游戏名称
    game_name_input = ('xpath', '//*[@placeholder="请输入游戏名称"]')

    # 计划状态
    plan_status_select = ('xpath', '//*[@placeholder="请选择计划状态"]')

    # 查询
    search_btn = ('css', '.el-form-item__content > .el-button--primary')

    # 重置
    reset_btn = ('css', '.el-form-item__content > .el-button--default')

    # 展开
    more_query_btn = ('css', '.el-button--text:nth-child(3) > span')

    # 新建试玩计划
    creat_play_plan_btn = ('id', 'gamePlayPlanList-add')


global page


class GamePlayPlanPage(BasePage):
    """
    试玩计划
    """
    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = GamePlayPlanActivity()

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
            time.sleep(2)

    def is_more_query(self):
        """
        检查是否为更多查询条件
        """
        return self.wait_exist(page.plan_status_select)

    def click_creat_play_plan(self):
        """
        点击新增试玩计划
        """
        self.click_element(page.creat_play_plan_btn)

    def view_play_plan(self, index=1):
        """
        查看试玩计划
        """
        # 查看
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[9]/div/div/button[1]'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)

    def edit_play_plan(self, index=1):
        """
        编辑试玩计划
        """
        # 编辑
        edit_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[9]/div/div/button[2]'.format(index))
        if self.wait_exist(edit_btn) and self.is_clickable(edit_btn):
            self.click_element(edit_btn)
            time.sleep(2)

    def close_play_plan(self, index=1):
        """
        终止试玩计划
        """
        # 终止试玩
        end_play_btn = ('', '//div[5]/div[2]/table/tbody/tr[{}]/td[9]/div/div/button[3]'.format(index))
        if self.wait_exist(end_play_btn) and self.is_clickable(end_play_btn):
            self.click_element(end_play_btn)
            time.sleep(2)

    def confirm_alter(self):
        """
        弹窗确认
        """
        self.click_element(('css', '.el-button--default:nth-child(2)'))
        time.sleep(2)

    def cancel_alter(self):
        """
        弹窗取消
        """
        self.click_element(('css', '.el-button--default:nth-child(1)'))
        time.sleep(2)
