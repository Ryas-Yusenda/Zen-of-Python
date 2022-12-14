from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime

# ======================= INPUT DATA ======================
LINK = "https://s.id/1ly0O"
NAMA = "Aaron"
EMAIL = "Aaron@gmail.com"
PARAGRAF = "Lorem ipsum, atau ringkasnya lipsum, adalah teks standar yang ditempatkan untuk mendemostrasikan elemen grafis atau presentasi visual seperti font, tipografi, dan tata letak."
DROP_DOWN = 3  # = "Opsi 3"
KOTAK_CENTANG = ["Y", "N", "Y", "KOTAK CENTANG LAINNYA"]
PILIHAN_GANDA = "PILIHAN GANDA LAINNYA"  # ATAU 1
TANGGAL = "10-13-2022"  # MM-DD-YY
WAKTU = ["15", "30"]  # 15.30
# =========================================================

# set chromodriver.exe path
driver = webdriver.Chrome(executable_path="./chromedriver.exe")


def nama():
    driver.find_element(
        By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(NAMA)


def email():
    driver.find_element(
        By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(EMAIL)


def paragraf():
    driver.find_element(
        By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea").send_keys(PARAGRAF)


def drop_down():
    driver.find_element(
        By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div").click()
    sleep(0.3)
    for i in range(1, DROP_DOWN+1):
        webdriver.ActionChains(driver).send_keys(Keys.DOWN).perform()
    webdriver.ActionChains(driver).send_keys(Keys.SPACE).perform()
    sleep(0.3)


def kotak_centang():
    data_centang = ["//*[@id='i22']/div[2]",
                    "//*[@id='i25']/div[2]",
                    "//*[@id='i28']/div[2]",
                    "//*[@id='mG61Hd']/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[4]/div/div/div/div/div[1]/input"]
    i = 1
    for centang in KOTAK_CENTANG:
        # print(centang)
        if centang == "Y":
            driver.find_element(By.XPATH, data_centang[i-1]).click()
        elif not (not centang) and i == int(len(KOTAK_CENTANG)):
            driver.find_element(By.XPATH, data_centang[i-1]).send_keys(centang)
        i += 1


def pilihan_ganda():
    data_pilih = ["//*[@id='i38']/div[3]/div",
                  "//*[@id='i41']/div[3]/div",
                  "//*[@id='i44']/div[3]/div",
                  "//*[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[4]/div/span/div/div/div[1]/input"]
    if type(PILIHAN_GANDA) == str:
        driver.find_element(By.XPATH, data_pilih[-1]).send_keys(PILIHAN_GANDA)
    else:
        driver.find_element(By.XPATH, data_pilih[PILIHAN_GANDA-1]).click()


def tanggal():
    driver.find_element(
        By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input").send_keys(TANGGAL)


def waktu():
    driver.find_element(
        By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input").send_keys(WAKTU[0])
    driver.find_element(
        By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input").send_keys(WAKTU[1])


def screenshot():
    driver.save_screenshot(
        'screenshots/checkBox_{0}.png'.format(datetime.now().strftime("%Y-%m-%d-%H-%M-%S")))


def kirim():
    driver.find_element(
        By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span").click()


# ====================== START CHROME =====================
driver.get(LINK)
# driver.maximize_window()
sleep(0.2)
nama()
email()
paragraf()
drop_down()
screenshot()
kotak_centang()
pilihan_ganda()
tanggal()
waktu()
screenshot()
kirim()
screenshot()

driver.quit()
