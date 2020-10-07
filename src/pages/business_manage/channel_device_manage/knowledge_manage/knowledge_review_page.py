"""
知识库审核
"""

import time

from src.pages.base_page import BasePage


class KnowledgeReviewActivity:
    # 物品类别
    device_type_select = ('xpath', '//*[@placeholder="请选择物品类别"]')

    # 故障类型
    failure_type_select = ('xpath', '//*[@placeholder="请选择故障类型"]')

    """
    审核
    """
    # 确认
    review_confirm = ('id', 'knowledgeBase-submit')
    # 取消
    review_cancel = ('id', 'knowledgeBase-cancel')


global page


class KnowledgeReviewPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = KnowledgeReviewActivity()

    def query_knowledge_review(self, device=None, failure=None):
        """
        查询
        :param device:
        :param failure:
        :return:
        """
        if device:
            self.select_pull_down_list(page.device_type_select, device)
        if failure:
            self.select_pull_down_list(page.failure_type_select, device)
        self.click_search_button()

    def read_query_device_type(self):
        """
        查看查询条件
        :return:
        """
        return self.get_text(page.device_type_select)

    def click_view_review_detail(self, index=1):
        """
        查看详情
        :return:
        """
        # 查看
        view_btn = ('xpath', '//div[@id="main"]/div/div/div[2]/div/div[5]/div[2]/table/tbody/tr[{}]/td[7]/div/button'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)

    def click_knowledge_review(self, index=1):
        """
        点击审核
        :return:
        """
        review = ('xpath', '//div[@id="main"]/div/div/div[2]/div/div[5]/div[2]/table/tbody/tr[{}]/td[7]/div/button[2]'.format(index))
        if self.wait_exist(review):
            self.click_element(review)
            time.sleep(2)

    def review_confirm(self, review=False):
        """
        审核确认操作
        :param review:
        :return:
        """
        if review:
            self.click_element(page.review_confirm)
        else:
            self.click_element(page.review_cancel)

    def click_delete_knowledge(self, index=1):
        """
        点击删除
        :return:
        """
        delete = ('xpath', '//div[@id="main"]/div/div/div[2]/div/div[5]/div[2]/table/tbody/tr[{}]/td[7]/div/button[3]'.format(index))
        if self.wait_exist(delete):
            self.click_element(delete)
            time.sleep(2)
