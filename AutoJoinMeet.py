from playwright.sync_api import Playwright, sync_playwright, expect
from threading import Event
import time

def nuke(acc,pas,meet_url):
    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        context.grant_permissions(permissions=['microphone','camera'])
        page = context.new_page()
        page.goto("https://accounts.google.com/ServiceLogin")
        page.locator("[aria-label=\"電子郵件地址或電話號碼\"]").click()
        page.locator("[aria-label=\"電子郵件地址或電話號碼\"]").fill(acc)
        with page.expect_navigation():
            page.locator("[aria-label=\"電子郵件地址或電話號碼\"]").press("Enter")
        page.locator("[aria-label=\"輸入您的密碼\"]").fill(pas)
        with page.expect_navigation():
            page.locator("[aria-label=\"輸入您的密碼\"]").press("Enter")
        page.goto(meet_url)
        page.locator("[aria-label=\"關閉麥克風 \\(Ctrl \\+ D\\)\"]").click()
        page.locator("[aria-label=\"關閉攝影機 \\(Ctrl \\+ E\\)\"]").click()
        page.locator("button:has-text(\"立即加入\")").click()
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
        input("按任意鍵關閉...")
        exit(0)
    meet_url = input("Google Meet 網址: ")
    nuke(acc,pas,meet_url)