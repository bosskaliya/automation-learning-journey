from itertools import count

from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()


        # Page definition
        print("Navigating to SauceDemo...")
        page.goto("https://www.saucedemo.com/")


        # Page interaction
        page.fill('[data-test="username"]', "standard_user")
        page.fill('[data-test="password"]', "secret_sauce")
        page.click('[data-test="login-button"]')

        # This was changed
        # print("Adding backpack to cart...")
        # page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
        # buttons = page.locator(".btn_inventory")
        #
        # count = buttons.count()
        # print(f"Found {count} item to add.")
        # Until here

        items = page.locator(".inventory_item")
        count = items.count()
        print(f"Found {count} items")

        for i in range(count):
            # Get the card at index i
            current_item = items.nth(i)

            # Find the "Add to cart: button INSIDE this specific card
            # We use specific text so we don't accidentally click "Remove" if we run this twice
            add_button = current_item.locator("button:has-text('Add to cart')")

            # Click it
            add_button.click()
            print(f"Clicked item #{i+1}")


        # cart_badge = page.locator('[data-test="shopping-cart-link"]')
        # if cart_badge.inner_text() == "1":
        #     print("SUCCESS: Item added to cart successfully!")
        # else:
        #     print(f"FAILURE: Cart shows {cart_badge.inner_text()}")

        # # THE LOOP
        # # We loop from index 0 to count-1
        # for i in range(count):
        #     buttons.nth(0).click()
        #     print(f"Clicked button #{i+1}")

        # Verify the Cart Badge shows '6'
        cart_badge = page.locator(".shopping_cart_badge")
        print(f"Cart now has: {cart_badge.inner_text()} items.")

        # Assert
        if cart_badge.inner_text() == "6":
            print("SUCCESS: All items added!")
        else:
            print("FAILURE: Count mismatch")


        browser.close()

if __name__ == "__main__":
    run()
