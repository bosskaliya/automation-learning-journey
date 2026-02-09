from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # 1. Lunch browser (Headless=False so you can see the magic)
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        # 2. Go to the login page
        print("Navigating to SauceDemo")
        page.goto("https://www.saucedemo.com/")

        # 3. INTERACTION: Fill in the Username
        # We use a CSS Selector here (id="user-name")
        page.fill("#user-name", "standard_user")

        # 4. INTERACTION: Fill in the Password
        page.fill("#password", "secret_sauce")
        # 5. INTERACTION: Click the Login Button
        print("Clicking Login...")
        page.click("#login-button")

        # 6. VERIFICATION: Did we succeed?
        # We check if the URL contains "inventory"
        if "inventory" in page.url:
            print("SUCCESS: Login passed!")
        else:
            print("FAILURE: Login failed.")
        # 7. Close
        browser.close()
if __name__ == "__main__":
    run()