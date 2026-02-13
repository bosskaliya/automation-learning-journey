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

            # B. Find the Price INSIDE this card
            price_element = current_item.locator(".inventory_item_price")
            price_text = price_element.inner_text()

            # C. CLEAN THE DATA
            clean_price = float(price_text.replace("$", ""))
            print(f"Checking Item #{i+1}: {clean_price}...")

            if clean_price < 15.00:
                print(" -> CHEAP! Adding to cart.")
                # Find the button inside THIS item and click it
                current_item.locator("button:has-text('Add to cart')").click()
            else:
                print(" -> Too expensive! Skipping.")

        # 4. VERIFY THE CART
        cart_badge = page.locator(".shopping_cart_badge")

        # We expect exactly 2 items (9.99 and 7.99)
        if cart_badge.inner_text() == "2":
            print("\nSUCCESS: Logic works! Exactly 2 items in cart.")
        else:
            print(f"\nFAILURE: Cart has {cart_badge.inner_text()} items. Expected 2.")

        browser.close()

if __name__ == "__main__":
    run()