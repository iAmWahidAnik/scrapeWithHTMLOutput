from django.shortcuts import render
from django.shortcuts import HttpResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Create your views here.
def show(request):
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://perfumancebd.com/product-category/perfume/refreshing/")
    titleList = []
    priceList = []
    for i in range(1, 12):
        # driver.get("https://perfumancebd.com/product-category/perfume/refreshing/")
        title = driver.find_element(by=By.XPATH, value='//*[@id="rig-adpr"]/div[' + str(i) + ']/p[1]').text
        price = driver.find_element(by=By.XPATH, value='//*[@id="rig-adpr"]/div[' + str(i) + ']/p[2]').get_attribute('innerHTML')

        titleList.append(title)
        priceList.append(price)

    myList = zip(titleList,priceList)
    scrape = {'Title':myList, 'Price':priceList}
    return render(request, 'daraz/form.html', context=scrape)