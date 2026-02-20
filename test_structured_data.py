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

            clean_price = float(price_text.replace("$", ""))

            # Logic
            if clean_price < 15.00:
                print(f"Item #{i+1} is ${clean_price} -> SAVING DATA")

                # --- THE UPGRADE ---
                # We create a "Packet" of data (A Dictionary
                item_data = {
                    "name": name_text,
                    "price": clean_price
                }

                # We add that packet to our list
                shopping_cart.append(item_data)
            else:
                print(f"Item #{i+1} is too expensive.")

        print("\n---------------------------------")
        print(f"FINAL REPORT: Found {len(shopping_cart)} cheap items.")
        print(shopping_cart)
        print("---------------------------------")

        browser.close()

if __name__ == "__main__":
    run()