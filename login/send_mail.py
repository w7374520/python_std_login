# import os
# from django.core.mail import send_mail
#
# os.environ['DJANGO_SETTINGS_MODULE'] = 'untitled.settings'
# #os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
#
# if __name__ == '__main__':
#     send_mail(
#         '来自www.lockv.com的测试邮件',
#         '欢迎访问http://www.lockv.com/,这里是wugq的博客',
#         'xxx@qq.com',
#         ['xxx@qq.com'],
#     )


import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'untitled.settings'

if __name__ == '__main__':
    subject, from_email, to = '来自www.lockv.com的测试邮件', 'xxx@qq.com', 'xxx@qq.com'
    text_content = '欢迎访问www.lockv.com， 这里是wugq的博客，专注python和django技术的分享!'
    html_content = '<p>欢迎访问<a href="http://www.lockv.com/" target=blank>www.lockv.com</a>, 这里是wugq的博客和教材，专注python和django技术的分享</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()