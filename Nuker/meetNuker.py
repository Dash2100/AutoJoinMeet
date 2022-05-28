from playwright.sync_api import Playwright, sync_playwright, expect
from threading import Event
import time

def nuke(acc,pas,meet_url,times):
    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False, args=['--use-fake-device-for-media-stream', '--use-fake-ui-for-media-stream'])
        context = browser.new_context()
        context.grant_permissions(permissions=['microphone'])
        page = context.new_page()
        page.goto("https://accounts.google.com/ServiceLogin")
        page.locator("[aria-label=\"電子郵件地址或電話號碼\"]").click()
        page.locator("[aria-label=\"電子郵件地址或電話號碼\"]").fill(acc)
        with page.expect_navigation():
            page.locator("[aria-label=\"電子郵件地址或電話號碼\"]").press("Enter")
        page.locator("[aria-label=\"輸入您的密碼\"]").fill(pas)
        with page.expect_navigation():
            page.locator("[aria-label=\"輸入您的密碼\"]").press("Enter")
        for _ in range(times):
            page = context.new_page()
            page.goto(meet_url)
            page.locator("[aria-label=\"關閉麥克風 \\(Ctrl \\+ D\\)\"]").click()
            page.locator("[aria-label=\"關閉攝影機 \\(Ctrl \\+ E\\)\"]").click()
            page.locator("button:has-text(\"立即加入\")").click()
            time.sleep(2)
        Event().wait()

    with sync_playwright() as playwright:
        run(playwright)

if __name__ == '__main__':
    # 在這裡輸入你的Google帳號密碼
    acc = ""
    pas = ""
    #----------------------------
    if acc == "" or pas =="":
        print("請用編輯器開啟並輸入你的Google帳號密碼")
        input()
        exit(0)
    meet_url = input("Google Meet 網址: ")
    times = int(input("數量: "))
    nuke(acc,pas,meet_url,times)