from itertools import count

from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 1. Login
        page.goto("https://www.saucedemo.com/")
        page.fill("[data-test='username']", "standard_user")
        page.fill("[data-test='password']", "secret_sauce")
        page.click("[data-test='login-button']")

        # --- NEW LOOP CODE GOES HERE ---

        # 2. Get the List of Cards (Parents)
        items = page.locator(".inventory_item")
        count = items.count()
        print(f"I found {count} items on the menu today:\n")

        # 3. The Loop
        for i in range(count):
            # A. Grab the specific card (The Scope)
            current_item = items.nth(i)

            # B. Find the Name INSIDE this card
            # Note: We use current_item.locator, NOT page.locator
            name_element = current_item.locator(".inventory_item_name")
            name_text = name_element.inner_text()

            # C. Find the Price INSIDE this card
            price_element = current_item.locator(".inventory_item_price")
            price_text = price_element.inner_text()

            # D. Print the result
            print(f"{i+1}: {name_text} costs {price_text}")

        browser.close()

if __name__ == "__main__":
    run()