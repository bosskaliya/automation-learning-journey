from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        print("Navigation to SauceDemo...")
        page.goto("https://www.saucedemo.com/")

        #Login Intersection
        page.fill('[data-test="username"]', "standard_user")
        page.fill('[data-test="password"]', "secret_sauce")
        page.click('[data-test="login-button"]')

        # 1. Add the Backpack to the cart
        print("Adding Backpack to cart...")
        page.click('[data-test="add-to-cart-sauce-labs-backpack"]')

        # 2. Get the next from the cart badge (The little red number)
        cart_badge = page.locator(".shopping_cart_badge")

        # 3. Check if the number is "1"
        if cart_badge.inner_text() == "1":
            print("SUCCESS: Item added to cart successfully!")
        else:
            print(f"FAILURE: Cart shows {cart_badge.inner_text()}")

        browser.close()

if __name__ == "__main__":
    run()
