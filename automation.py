from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

def scrape_quotes():

   
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")     # Browser hidden mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)


    url = "https://quotes.toscrape.com/"
    driver.get(url)
    time.sleep(2)

    quotes_elements = driver.find_elements(By.CLASS_NAME, "text")
    authors_elements = driver.find_elements(By.CLASS_NAME, "author")

    quotes = []
    authors = []

    for q, a in zip(quotes_elements, authors_elements):
        quotes.append(q.text)
        authors.append(a.text)

    
    df = pd.DataFrame({
        "Quote": quotes,
        "Author": authors
    })
    df.to_csv("output.csv", index=False)


    driver.quit()

    print("Scraping Successful! Data saved in output.csv")


if __name__ == "__main__":
    scrape_quotes()
