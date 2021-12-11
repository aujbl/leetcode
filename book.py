from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from tkinter import *

import time
import schedule
from tqdm import tqdm

import smtplib
from email.mime.text import MIMEText

global s
global len_inform
s = time.time()

has_inform = set()
len_inform = len(has_inform)
book_time = {
    '08:00-09:00': 0, '09:01-10:00': 0, '10:01-11:00': 0, '11:01-12:00': 0,
    '12:01-13:00': 0, '13:01-14:00': 0, '14:01-15:00': 0, '15:01-16:00': 0,
    '16:01-18:00': 0, '18:01-20:00': 1, '20:01-22:00': 1
}
book = [k for k, v in book_time.items() if v == 1]


def show_message(text):
    # show reminder message window
    root = Tk()  # 建立根窗口
    # root.minsize(500, 200)   #定义窗口的大小
    # root.maxsize(1000, 400)  #不过定义窗口这个功能我没有使用
    root.withdraw()  # hide window
    # 获取屏幕的宽度和高度，并且在高度上考虑到底部的任务栏，为了是弹出的窗口在屏幕中间
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight() - 100
    root.resizable(False, False)
    # 添加组件
    root.title("booking!!")
    frame = Frame(root, relief=RIDGE, borderwidth=3)
    frame.pack(fill=BOTH, expand=1)  # pack() 放置组件若没有则组件不会显示
    # 窗口显示的文字、并设置字体、字号
    label = Label(frame, text=text)
    label.pack(fill=BOTH, expand=1)
    # 按钮的设置
    button = Button(frame, text="OK", font="Cooper -25 bold", fg="red", command=root.destroy)
    button.pack(side=BOTTOM)

    root.update_idletasks()
    root.deiconify()  # now the window size was calculated
    root.withdraw()  # hide the window again 防止窗口出现被拖动的感觉 具体原理未知？
    root.geometry('%sx%s+%s+%s' % (root.winfo_width() + 10, root.winfo_height() + 10,
                                   (screenwidth - root.winfo_width()) // 2,
                                   (screenheight - root.winfo_height()) // 2))
    root.deiconify()
    root.mainloop()


def silent(flag=True):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('log-level=3')

    return options


def mail(text=None):
    # 设置服务器所需信息
    # 163邮箱服务器地址
    mail_host = 'smtp.qq.com'
    # 163用户名
    mail_user = '953486511@qq.com'
    # 密码(部分邮箱为授权码)
    mail_pass = 'lazvodsfjvmpbeii'
    # 邮件发送方邮箱地址
    sender = '953486511@qq.com'
    # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = ['aujblee@foxmail.com']

    # 设置email信息
    # 邮件内容设置
    message = MIMEText(text, 'plain', 'utf-8')
    # 邮件主题
    message['Subject'] = '订场'
    # 发送方信息
    message['From'] = sender
    # 接受方信息
    message['To'] = receivers[0]

    # 登录并发送邮件
    try:
        # smtp = smtplib.SMTP()
        # # 连接到服务器
        # smtp.connect(mail_host, 25)

        smtp = smtplib.SMTP_SSL(mail_host)

        # 登录到服务器
        smtp.login(mail_user, mail_pass)
        # 发送
        smtp.sendmail(
            sender, receivers, message.as_string())
        # 退出
        smtp.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('error', e)  # 打印错误


def main(m=True, show=True):
    global s
    global len_inform
    options = silent()
    # 创建 WebDriver 对象，指明使用chrome浏览器驱动
    s = Service(r'd:\chromedriver\chromedriver.exe')
    wd = webdriver.Chrome(service=s, options=options)

    # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
    wd.get('http://116.57.72.197:9099/product/show.html?id=346')

    # element = wd.find_element(By.CLASS_NAME, 'stock')
    elements = wd.find_elements(By.CSS_SELECTOR, '[data-name*="场地"]')

    # if int(element.text.split()[-1]) > 0:
    #     sho_message(element.text)
    text = ''
    for e in elements:
        if e.get_attribute('data-did') and e.get_attribute('data-timer') in book:
            name = e.get_attribute('data-name')
            timer = e.get_attribute('data-timer')
            has_inform.add((name + timer))
            text += name + '\t\t' + timer + '\n'

    if len(has_inform) > len_inform:
        len_inform = len(has_inform)
        if m:
            mail(text)
        if show:
            show_message(text)
    else:
        print('.....')
        # print('%.1f' % (time.time() - s), 's')
        # s = time.time()
        # print("no site.")

    wd.quit()


if __name__ == '__main__':
    main()
    schedule.every(10).to(30).seconds.do(main)
    # schedule.every(5).to(10).minutes.do(main)
    while True:
        try:
            schedule.run_pending()
        except KeyboardInterrupt:
            print('quit')
            break
        except Exception:
            show_message("wrong!")

    # main()
