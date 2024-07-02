import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import warnings
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import ctypes
import pyperclip
import pywinauto
from pywinauto.keyboard import send_keys
import os


def copy_text(text):
    pyperclip.copy(text)


def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)


set_console_title("keji autoXGP")
warnings.filterwarnings('ignore')


def randomUsername(length=16):
    base_Str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    random_str = ''
    for i in range(length):
        random_str += base_Str[random.randint(0, (len(base_Str) - 1))]
    return random_str


def purchasecheck():
    try:
        success = driver.find_element(By.XPATH,
                                      '/html/body/reach-portal/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]/div[3]/a')
        success = int(success)
        if success == '<selenium.webdriver.remote.webelement.WebElement (session="9a245c8242c7806aae13821738d81698", element="23F5752506E09117C6B47DABC432C962_element_221")>':
            s = 1
        else:
            s = 2
    except NoSuchElementException:
        print('等待中......')
        s = 2
        return False


print('''
██╗  ██╗███████╗     ██╗██╗     █████╗ ██╗   ██╗████████╗ ██████╗ ██╗  ██╗ ██████╗ ██████╗ 
██║ ██╔╝██╔════╝     ██║██║    ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗╚██╗██╔╝██╔════╝ ██╔══██╗
█████╔╝ █████╗       ██║██║    ███████║██║   ██║   ██║   ██║   ██║ ╚███╔╝ ██║  ███╗██████╔╝
██╔═██╗ ██╔══╝  ██   ██║██║    ██╔══██║██║   ██║   ██║   ██║   ██║ ██╔██╗ ██║   ██║██╔═══╝ 
██║  ██╗███████╗╚█████╔╝██║    ██║  ██║╚██████╔╝   ██║   ╚██████╔╝██╔╝ ██╗╚██████╔╝██║     
╚═╝  ╚═╝╚══════╝ ╚════╝ ╚═╝    ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝                                                                                         
[+]自动刷XGP机
[+]使用时请使用新号
[+]请挂好香港VPN
[+]唯一手动的地方就是扫码登录以及确认协议
[+]版本1.0
''')

acc = input('邮箱----密码:')
parts = acc.split("----")
Email = parts[0]
Password = parts[1]
print("请使用新号")
print("除了要求请问擅自操作页面))")
Xbox_User = 'AzusaZi' + randomUsername(6)
IGN = 'A' + randomUsername(2) + 'D' + randomUsername(2)

edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = False
edge_options.add_experimental_option('useAutomationExtension', False)
edge_options.add_argument('--inprivate')
edge_options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])

driver = webdriver.Edge('msedgedriver.exe', options=edge_options)
print('即将打开浏览器并自动购买......')
driver.get('https://www.xbox.com/zh-HK/xbox-game-pass#join')
print("在页面上查找29港币的PC Game pass")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "a[data-xbbigid='CFQ7TTC0KGQ8']").click()
WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.NAME, 'loginfmt'))).send_keys(Email)
print('自动输入邮箱密码登录')
print("点击下一步")
next_button = driver.find_element(By.ID, 'idSIButton9').click()
time.sleep(2)
print("输入密码")
WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.NAME, 'passwd'))).send_keys(Password)
print("点击登录")
WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.ID, 'idSIButton9'))).click()
print("点击保持登录状态。15s")
WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.ID, 'idSIButton9'))).click()
time.sleep(15)
try:
    print("输入Xbox用户名")
    print('即将自动设置Xbox用户名......（15sec）')
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, 'create-account-gamertag-input'))).send_keys(Xbox_User)
    print("确认ID有效之后按下回车(不要操作页面！)")
    b = input("")
    print("你已经确认")
    print("点击开始按钮...8sec")
    WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.ID, 'inline-continue-control'))).click()
    time.sleep(4)
    print("正在跳过按钮")
    driver.get('https://www.xbox.com/zh-HK/xbox-game-pass?launchStore=CFQ7TTC0KGQ8#join')
    time.sleep(4)
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//button[@aria-label="下一步"]'))).click()
except TimeoutException:
    print("没有发现取名页面,点击下一步按钮")
    WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, '//button[@aria-label="下一步"]'))).click()
    time.sleep(8)
print('即将自动添加支付宝付款')
driver.switch_to.frame('purchase-sdk-hosted-iframe')
WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="optionContainer--A9GXUhvU lightweight--IYKcwqan base--kY64RzQE"]'))).click()
time.sleep(2)
print("选择Alipay支付")

time.sleep(5)
try:
    WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="displayId_ewallet"]'))).click()
    WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="displayId_ewallet_alipay_billing_agreement"]'))).click()
    try:
        print("下一步")
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, '//input[@aria-label="下一步"]'))).click()
        time.sleep(4)
    except NoSuchElementException:
        print("错误")
except NoSuchElementException:
    print("没有发现二维码，可能之前你已经开通过了，请确认页面位于支付宝签约二维码处，然后点击回车")
    print("如果你发现页面上面已经有一个支付宝选项 则说明这个账号已经有人绑定过支付宝了 如果确定继续，请按照如下步骤操作:")
    print("1，点击确定")
    print("2.点击新增付款方式")
    a = input("3.选择支付宝 确认页面位于支付宝签约二维码处，然后点击回车")
WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pidlddc-image-alipayQrCodeChallengeImage"]'))).click()
print('等待支付宝扫码...')
print("开通后按回车")
a = input("")
print("你已经手动确认")
print("点击继续")
continue_button = driver.find_element(By.ID, 'pidlddc-button-alipayContinueButton').click()
time.sleep(3)
try:
    print("输入城市 and 地址")
    WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.ID, 'city'))).send_keys('1')
    WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.ID, 'address_line1'))).send_keys('1')
    print("储存")
    save_button = driver.find_element(By.ID, 'pidlddc-button-saveButton').click()
    time.sleep(12)
except NoSuchElementException:
    print("未发现设置地址的页面")
    pass
print("点击订阅按钮")
WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.XPATH, "/html/body/section/div[1]/div/div/div/div/div[2]/div/div[4]/button[2]"))).click()
print("等待购买成功")
time.sleep(18)
'''while s == 1:
        pass
    else:
        print("等待购买结果中")'''
print('购买成功!')
print('即将为您自动设置ID')
driver.get('https://www.minecraft.net/en-us/msaprofile/mygames/editprofile')
time.sleep(10)

WebDriverWait(driver, 2000).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#LoginAnimation_Bee > div.container > div > div > section > div:nth-child(3) > div > div.login-form-view__first-container.p-4.d-flex.flex-column.justify-content-between > div:nth-child(1) > div > a"))).click()
WebDriverWait(driver, 2000).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='profileName']"))).send_keys('Genshin_' + IGN)

try:
    WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='Set up your Profile Name']"))).click()
except NoSuchElementException:
    print('按钮不可用')
    time.sleep(4)
    WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='Set up your Profile Name']"))).click()
time.sleep(6)
print('[ID设置成功! ID为:' + 'Genshin_' + IGN)


print('设置完成')
print('即将打开退款链接并自动退款,需要手动确认链接')
driver.get('https://account.microsoft.com/services/pcgamepass/cancel?fref=billing-cancel&lang=en-US')
time.sleep(20)
try:
    WebDriverWait(driver, 2000).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='Cancel subscription']"))).click()
except NoSuchElementException:
    driver.implicitly_wait(5)
    WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.ID, 'id__0'))).click()
    WebDriverWait(driver, 2000).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='Cancel subscription']"))).click()
refund_button = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Cancel now and get refund']").click()
cancel_button = driver.find_element(By.ID, 'cancel-select-cancel').click()
time.sleep(15)
print('已经成功退款！')
print('正在保存')
input('按回车键退出程序。')
with open("accounts.txt", "a") as f:
    f.write(f"{Email}----{Password}----{'Genshin_' + IGN}\n")
