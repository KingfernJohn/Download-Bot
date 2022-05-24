try:
    import selenium
    import time, os
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
except:
    print()
    print("ERROR!")
    print("Please install the modules in requirements.txt")
    input("Press Enter to Exit ")
    quit()
print("""
  _____   ______          ___   _ _      ____          _____             ____   ____ _______ 
 |  __ \ / __ \ \        / / \ | | |    / __ \   /\   |  __ \           |  _ \ / __ \__   __|
 | |  | | |  | \ \  /\  / /|  \| | |   | |  | | /  \  | |  | |  ______  | |_) | |  | | | |   
 | |  | | |  | |\ \/  \/ / | . ` | |   | |  | |/ /\ \ | |  | | |______| |  _ <| |  | | | |   
 | |__| | |__| | \  /\  /  | |\  | |___| |__| / ____ \| |__| |          | |_) | |__| | | |   
 |_____/ \____/   \/  \/   |_| \_|______\____/_/    \_\_____/           |____/ \____/  |_|                                                                            
  """)
print()
print("DOWNLOAD-BOT by KingfernJohn")
print()
file_size = input("Enter 'b' for normal sized files & 's' for small files: ")
print()
starget = int(input("TARGET-DOWNLOAD.AMOUNT: "))+1
stargetadr = input("TARGET-WEB.DOWNLOAD.ADRES: ")
stargetdwnl = input("/Users/ *USER* /Downloads/ *FILE_NAME*  - so the downloaded files get deleted: ")
file_path = stargetdwnl
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 3)
visible = EC.visibility_of_element_located
browser.get(stargetadr)
if file_size == "b":
    for x in range(starget):
        time.sleep(10)
        if os.path.exists(file_path):
            os.remove(file_path)
        browser.refresh()
        time.sleep(10)
        if os.path.exists(file_path):
            os.remove(file_path)
    browser.quit()
if file_size == "s":
    for x in range(starget):
        time.sleep(5)
        if os.path.exists(file_path):
            os.remove(file_path)
        browser.refresh()
        time.sleep(5)
        if os.path.exists(file_path):
            os.remove(file_path)    
    browser.quit()
