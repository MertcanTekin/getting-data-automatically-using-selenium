from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import zipfile
import os
import time
import glob


driver = webdriver.Chrome()
driver.get("https://www.floridaucc.com/uccweb/downloadsdisclaimer.aspx")

try:
    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "AcceptCheckbox"))
    )
    checkbox.click()
    print("Clicked successfully")
except:
    print("error")
try:
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "nextButton"))
    )
    next_button.click()
    print("Clicked successfully.")
except:
    print("error")

try:
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "rbDwnLoadType2"))
    )
    next_button.click()
    print("Clicked Successfully")
except:
    print("error")
    
try:
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "downloadRadioButton1"))
    )
    next_button.click()
    print("clicked successfully")
except:
    print("Error") 
    
    
try:
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "DownloadButton"))
    )
    next_button.click()
    print("Clicked Successfully")
except:
    print("Error")        

try:
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "downloadRadioButton2"))
    )
    next_button.click()
    print("Clicked Successfully")
except:
    print("Error")   
try:
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "DownloadButton"))
    )
    next_button.click()
    print("Clicked Successfully")
except:
    print("Error")   

try:
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "downloadRadioButton3"))
    )
    next_button.click()
    print("Clicked Successfully")
except:
    print("Error")       
    
try:
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "DownloadButton"))
    )
    next_button.click()
    print("Clicked Successfully")
except:
    print("Error")   
    
try:
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "downloadRadioButton4"))
    )
    next_button.click()
    print("Clicked Successfully")
except:
    print("Error")       
        
try:
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "DownloadButton"))
    )
    next_button.click()
    print("Clicked Successfully")
except:
    print("Error")  


time.sleep(800)   #setting time to wait files to be downloaded


driver.quit()



#it finds the last 4 zip files
download_folder = "C:/Users/user/Downloads"
zip_files = sorted(glob.glob(os.path.join(download_folder, "*.zip")), key=os.path.getctime, reverse=True)[:4]

#determine output folder
output_folder = "C:/Users/user/Desktop/Yeni klasör (2)"
os.makedirs(output_folder, exist_ok=True)

for zip_file in zip_files:
    
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        
        for txt_file in zip_ref.namelist():
            if txt_file.endswith(".txt"):
                zip_ref.extract(txt_file, output_folder)

print("last 4 zip files extracted successfully ")





def readbypiece(file_path, size):
    with open(file_path, "r", encoding="utf-8", errors="replace") as file:
        while True:
            piece = file.read(size)
            if not piece:
                break
            print(piece)


folder_path = "C:/Users/user/Desktop/Yeni klasör (2)"  # the folder that includes last 4 txt files

file_names = os.listdir(folder_path)

# make a path list to read the data
txt_files = []
for file_name in file_names:
    if file_name.endswith(".txt"):
        file_path = os.path.join(folder_path, file_name)
        txt_files.append(file_path)

size = 1024 * 1024 * 100  # 100 MB

for txt_file in txt_files[:4]:
    try:
        readbypiece(txt_file, size)
    except FileNotFoundError:
        print(f"File '{txt_file}' has not been found")
    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError error in file '{txt_file}': {e}")















   








