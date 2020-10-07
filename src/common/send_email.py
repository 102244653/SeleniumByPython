
import smtplib
import argparse
from email.header import Header
from email.mime.text import MIMEText
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# 发件人和收件人
sender = 'Test_Automation@genlot.com'
receiver = 'hct_xf@163.com'
 
# 发送邮箱的用户名和授权码（不是登录邮箱的密码）
username = 'Test_Automation@genlot.com'
password = 'Genlot123'

# 邮件主题
mail_title = '福乐彩运营管理平台自动化测试报告'
 
# 读取html文件内容
mail_body = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>福乐彩运营管理平台自动化测试报告</title>
</head>

<body leftmargin="8" marginwidth="0" topmargin="8" marginheight="4" offset="0">
    <table width="95%" cellpadding="0" cellspacing="0" style="font-size: 11pt; font-family: Tahoma, Arial, Helvetica, sans-serif">
		<tr>
			<td>福乐彩运营管理平台自动化测试报告，请查收！(本邮件由程序自动下发，请勿回复！)</td>
		</tr>

        <tr>
            <td><br />
                <b><font color="#0B610B">报告详情：</font></b>
                <hr size="2" width="100%" align="center" />
            </td>
        </tr>
        <tr>   
            <td>
                <ul>
                    <li>项目名称：福乐彩运营管理平台</li>
                    <li>测试环境：TEST</li>   
					<li>测试浏览器：Chrome</li>  
                    <li>报告链接：<a href="http://10.36.0.68:8989/build_number/">VLT_WEB自动化测试报告</a></li>
                </ul>
            </td>
        </tr>
 
    </table>

</body>
</html>
'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='build_number')
    parser.add_argument("--id", type=str, default="1")
    args = parser.parse_args()
    number = args.id
    # 邮件内容, 格式, 编码
    message = MIMEText(mail_body, 'html', 'utf-8')
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header(mail_title.replace('build_number', number), 'utf-8')

    # try:
    #
    # except Exception as e:
    #     print("邮件发送失败!", e)
    server = smtplib.SMTP_SSL()  # 在阿里云上python2.7以上需要使用SSL协议
    server.connect('smtp.mxhichina.com', port=465)  # 阿里云25 和80 端口均被使用 465端口使用 SSL协议
    server.login(username, password)
    server.sendmail(sender, receiver, message.as_string())
    server.close()
    print("邮件发送成功!")
