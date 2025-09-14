import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

def scrape_data():
    url = "https://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    titles = [book.h3.a["title"] for book in soup.find_all("article", class_="product_pod")]
    prices = [float(book.find("p", class_="price_color").text[2:]) for book in soup.find_all("article", class_="product_pod")]

    data = pd.DataFrame({"Title": titles, "Price": prices})
    data.to_csv("books.csv", index=False)
    print("✅ Data saved to books.csv")
    return data

def visualize_data(data):
    plt.figure(figsize=(8,6))
    data["Price"].plot(kind="hist", bins=10, rwidth=0.8)
    plt.title("Book Price Distribution")
    plt.xlabel("Price")
    plt.ylabel("Count")
    plt.savefig("books_chart.png")
    plt.show()
    print("📊 Chart saved as books_chart.png")

if __name__ == "__main__":
    data = scrape_data()
    visualize_data(data)
