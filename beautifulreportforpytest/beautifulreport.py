import json
import os
import platform
import time


class BeautifulConfig:
    template_path = os.path.join(os.path.dirname(__file__), 'template')
    config_tmp_path = os.path.join(template_path, 'template.html')
    img_path = None
    report_path = None
    is_ui = True

    @staticmethod
    def init_dir():
        # 项目根目录生成一个报告文件夹report，图片文件夹img:  /report/img
        path = os.path.split(os.path.realpath(__file__))[0][:-24]
        os.makedirs(path+'/beautifulreport/img', exist_ok=True)
        BeautifulConfig.img_path = path+'/beautifulreport/img'
        BeautifulConfig.report_path = path + '/beautifulreport'


class BeautifulResult:
    def __init__(self):
        self.default_report_name = '自动化测试报告'
        self.begin_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.start_time = 0
        self.end_time = 0
        self.all_case_counter = 0
        self.success_case_info = []
        self.skipped_case_info = []
        self.failures_case_info = []
        self.result_list = []
        self.fields = {
            "testPass": 0,
            "testResult": [],
            "testName": "",
            "testAll": 0,
            "testFail": 0,
            "beginTime": "",
            "totalTime": "",
            "testSkip": 0
        }

    @property
    def counter_success(self):
        return len(self.success_case_info)

    @property
    def counter_fail(self):
        return len(self.failures_case_info)

    @property
    def counter_skip(self):
        return len(self.skipped_case_info)

    @property
    def counter_all(self):
        return self.counter_fail+self.counter_skip+self.counter_success

    @property
    def total_time(self):
        self.end_time = int(time.time())
        total = self.end_time - self.start_time
        if total < 60:
            return str(total) + 's'
        elif total < 3600:
            return str(int(total/60)) + 'M ' + str(total % 60) + 's'
        else:
            _t = total % 3600
            return str(int(total / 3600)) + 'H ' + str(int(_t/60)) + 'M ' + str(_t % 60) + 's'

    def stop_test_run(self, title=None):
        """
            所有测试执行完成后, 执行该方法
        :param title:
        :return:
        """
        self.fields['testName'] = title if title else self.default_report_name
        self.fields['testPass'] = self.counter_success
        self.fields['testFail'] = self.counter_fail
        self.fields['testSkip'] = self.counter_skip
        self.fields['testError'] = '0'
        self.fields['testAll'] = self.counter_all
        self.fields['beginTime'] = self.begin_time
        self.fields['totalTime'] = self.total_time

        for item in self.result_list:
            item = json.loads(str(json.dumps(item.__dict__)))
            self.fields.get('testResult').append(item)
        return self.fields


beautiful = BeautifulResult()


class CaseResult:

    def __init__(self):
        self.className = None
        self.methodName = None
        self.description = None
        self.spendTime = None
        self.status = None
        self.log = []


class BeautifulReport:
    img_path = 'img/' if platform.system() != 'Windows' else 'img\\'

    def __init__(self):
        self.report_dir = BeautifulConfig.report_path
        self.title = '自动化测试报告'
        self.filename = '{}.html'.format(beautiful.default_report_name)
        self.result_json = ''

    def report(self, beautiful, description, log_path=None, theme='theme_default'):
        """
            生成测试报告,并放在当前运行路径下
        :param report_dir: 生成report的文件存储路径
        :param filename: 生成文件的filename
        :param description: 生成文件的注释
        :param theme: 报告主题名 theme_default theme_cyan theme_candy theme_memories
        :return:
        """
        if log_path:
            import warnings
            message = ('"log_path" is deprecated, please replace with "report_dir"\n'
                       "e.g. result.report(filename='测试报告_demo', description='测试报告', report_dir='report')")
            warnings.warn(message)

        if self.filename:
            self.filename = self.filename if self.filename.endswith('.html') else self.filename + '.html'

        if description:
            self.title = description

        self.result_json = beautiful.stop_test_run(self.title)
        self.output_report(theme)
        text = '\n测试已全部完成, 可打开 {} 查看报告'.format(os.path.join(self.report_dir, self.filename))
        print(text)

    def output_report(self, theme):
        """
            生成测试报告到指定路径下
        :return:
        """

        def render_template(params: dict, template: str):
            for name, value in params.items():
                name = '${' + name + '}'
                template = template.replace(name, value)
            return template

        template_path = BeautifulConfig.config_tmp_path
        with open(os.path.join(BeautifulConfig.template_path, theme + '.json'), 'r') as theme:
            render_params = {
                **json.load(theme),
                'resultData': json.dumps(self.result_json, ensure_ascii=False, indent=4)
            }

        override_path = os.path.abspath(self.report_dir) if \
            os.path.abspath(self.report_dir).endswith('/') else \
            os.path.abspath(self.report_dir) + '/'

        with open(template_path, 'rb') as file:
            body = file.read().decode('utf-8')
        with open(override_path + self.filename, 'w', encoding='utf-8', newline='\n') as write_file:
            html = render_template(render_params, body)
            write_file.write(html)


