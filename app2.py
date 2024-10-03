from selenium import webdriver
from selenium.webdriver.common.by import By

# WebDriverをセットアップ
driver = webdriver.Chrome()

try:
    # Yahoo Japanに移動
    driver.get('https://www.yahoo.co.jp/')

    # メインセクションのトップニュース記事を取得
    top_news_elements = driver.find_elements(By.CLASS_NAME, '_2j0udhv5jERZtYzddeDwcv')

    # 各要素から最初のテキストを抽出して表示
    for news in top_news_elements:
        first_text = news.text.split("\n")[0]  # 改行でテキストを分割し、最初の行を取得
        print(first_text)

finally:
    # ブラウザを閉じる
    driver.quit()
