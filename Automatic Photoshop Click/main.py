import pyautogui
import time
import timeit
import os

# print(pyautogui.size())
# time.sleep(3)
# print(pyautogui.position())
# time.sleep(3)
# print(pyautogui.position())
# time.sleep(3)
# print(pyautogui.position())

LIST_FOLDER = [
    "D:/Data/Desktop/ps/h7_3",
    "D:/Data/Desktop/ps/h14_1",
    "D:/Data/Desktop/ps/h14_2",
    "D:/Data/Desktop/ps/h14_3",
]

if False:
    #  POSISI LAYAR PHOTOSHOP DIKIRI DARI SETENGAH LAYAR LAPTOP
    for folder in LIST_FOLDER:
        tic_all = timeit.default_timer()
        pyautogui.click(x=24, y=606)
        #  LOKASI FOLDER
        LIST = os.path.normpath(folder)

        #  HITUNG JUMLAH FILE DI FOLDER
        NUM_REQ = 0
        for root_dir, cur_dir, files in os.walk(folder):
            NUM_REQ += len(files)

        print('\n({0}) <==> "{1}"'.format(NUM_REQ, LIST))

        #  BUKA FOLDER/FILE
        pyautogui.click(x=24, y=606)  # KLIK PHOTOSHOP
        pyautogui.keyDown('ctrl')
        pyautogui.press('o')  # POP_UP OPEN
        pyautogui.keyUp('ctrl')
        time.sleep(2)

        #  PASTE LOCATION
        pyautogui.click(x=242, y=479)  # FILE NAME
        pyautogui.typewrite(LIST)
        time.sleep(1)
        pyautogui.click(x=776, y=508)  # OPEN
        time.sleep(1)

        #  PILIH SEMUA FILE
        pyautogui.click(x=607, y=307)  # FILE SLECT
        time.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.press('a')  # POP_UP OPEN
        pyautogui.keyUp('ctrl')
        time.sleep(1)
        pyautogui.click(x=776, y=508)  # OPEN

        # WAKTU TUNGGU MENGIMPORT FILE
        time.sleep(100)

        pyautogui.click(x=24, y=606)
        pyautogui.press('w')

        for i in range(0, NUM_REQ):
            time.sleep(3)
            # WAKTU PROSES
            tic = timeit.default_timer()

            # BAGIAN KIRI
            pyautogui.click(x=269, y=525)
            pyautogui.press('delete')  # POP_UP CONTENT-AWARE
            time.sleep(1)
            pyautogui.click(1089, 291)  # OKE
            time.sleep(7)

            # BAGIAN KANAN
            pyautogui.click(x=586, y=521)
            pyautogui.press('delete')  # POP_UP CONTENT-AWARE
            time.sleep(1)
            pyautogui.click(1089, 291)  # OKE
            time.sleep(7)

            # CLOSE FOTO
            time.sleep(1)
            pyautogui.click(x=24, y=606)
            pyautogui.keyDown('ctrl')
            pyautogui.press('w')  # POP_UP SAVE BEFORE CLOSE
            pyautogui.keyUp('ctrl')
            time.sleep(1)
            pyautogui.click(x=380, y=395)  # YES

            # SIMPAN FOTO
            time.sleep(1)
            pyautogui.click(1068, 262)  # OK

            # WAKTU PROSES
            toc = timeit.default_timer()
            print('{0}/{3} in {1} seconds from {2}'.format(i+1,
                  round(toc - tic, 4), round(toc - tic_all, 4), NUM_REQ))

      #   PAUSE PERPINDAHAN OPEN FOLDER
        time.sleep(2)
    pyautogui.alert(text='DONE!!', title='Finish', button='OK')
