from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # 1. Launch browser
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        # 2. Go to website
        print("Navigating to Google...")
        page.goto("https://www.google.com/")

        # 3. Get the title
        title = page.title()
        print(f"Page title is: {title}")

        # 4. Close browser
        browser.close()

if __name__ == "__main__":
    run()