from selenium import webdriver  
import csv
chrome_path = r"C:\Users\WINDOWS\Desktop\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vSc_2y5N0I67wDU38DjDh35IZSIS30rQf7_NYZhtYYGU1jJYT6_kDx4YpF-qw0LSlGsBYP8pqM_a1Pd/pubhtml#")

driver.find_element_by_xpath("""//*[@id="0"]/div/table""").click()

num_of_rows = len(driver.find_elements_by_xpath( """//*[@id="0"]/div/table/tbody/tr""" ))
num_of_cols = len(driver.find_elements_by_xpath( """//*[@id="0"]/div/table/tbody/tr[3]/td""" ))

csv_row = []   

with open(r'C:\Users\WINDOWS\Desktop\corona_data.csv', 'w', newline = "") as csvFile:
	writer = csv.writer(csvFile, delimiter = ',')
	for r in range(1, num_of_rows+1):
		for c in range(1, num_of_cols+1):
			value = driver.find_element_by_xpath("""//*[@id="0"]/div/table/tbody/tr["""+str(r)+"""]/td["""+str(c)+"""]""").text
			csv_row.append(value)	
		writer.writerow(csv_row) 
		csv_row = []           		 
	csvFile.close()
