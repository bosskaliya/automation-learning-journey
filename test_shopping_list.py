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

        # 2. Get Items
        items = page.locator(".inventory_item")
        count = items.count()

        # --- CHANGE #1: Create the empty list (The Shopping Cart) ---
        shopping_cart = []
        print(f"Starting analysis of {count} items...\n")

        # 3. The Loop
        for i in range(count):
            current_item = items.nth(i)

            # Get Name & Price
            name_text = current_item.locator(".inventory_item_name").inner_text()
            price_text = current_item.locator(".inventory_item_price").inner_text()

            # Clean Price
            clean_price = float(price_text.replace("$", ""))

            # Logic
            if clean_price < 15.00:
                print(f"Item #{i+1} ({name_text}) is ${clean_price} -> ADDING TO LIST")

                # --- CHANGE #2: Add to the List instead of clicking---
                shopping_cart.append(name_text)

            else:
                print(f"Item #{i+1} is too expensive ({clean_price})")

        # --- CHNAGE #3: Print the final result (OUTSIDE the loop) ---
        print("\n---------------------------------")
        print(f"FINAL SHOPPING LIST:")
        print(shopping_cart)
        print("\n---------------------------------")

        browser.close()

if __name__ == "__main__":
    run()

