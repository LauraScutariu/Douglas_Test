# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
#
# lista_produse = ["DIOR Forever No-Transfer 24h Wear Matte Foundation", "IT Cosmetics Heavenly Luxe Complexion Brush #7", "Prada Paradoxe Eau de Parfum Refillable"]
#
# for produs in lista_produse:
#     search_box = driver.find_element("id", "//input[@type='search']")
#     search_box.clear()
#     search_box.send_keys(produs)
#     search_box.send_keys(Keys.RETURN)
#
#     time.sleep(3)
#
#     add_to_cart_button = driver.find_element("xpath", "//button[@class='btn btn-block btn-buy e-btn-buy'']")
#     add_to_cart_button.click()
#
# driver.quit()