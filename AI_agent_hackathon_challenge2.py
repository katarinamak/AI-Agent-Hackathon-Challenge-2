import requests
from bs4 import BeautifulSoup
import PyPDF2
from selenium import webdriver
import sys
import io


def download_pdf():
    # Step 1: Fetch the webpage content

    url = "https://ocw.mit.edu/courses/2-016-hydrodynamics-13-012-fall-2005/resources/hw1"
    
    response = requests.get(url)
    html_content = response.text

    # Step 2: Parse the HTML content to find PDF links
    soup = BeautifulSoup(html_content, 'html.parser')
    pdf_links = []

    for link in soup.find_all('a'):
        href = link.get('href')
        # print(href)
        if href.endswith('.pdf'):
            pdf_links.append(href)

    # Step 3: Choose a PDF link (you can select one from the pdf_links list)
    if pdf_links:
        pdf_url = pdf_links[0]  # Choose the first PDF link, for example
        pdf_response = requests.get("https://ocw.mit.edu" + pdf_url)

        # Step 4: Save the PDF to a local file (optional)
        with open('downloaded.pdf', 'wb') as pdf_file:
            pdf_file.write(pdf_response.content)

        # Step 5: Open the PDF in the default PDF viewer using Selenium
        driver = webdriver.Chrome()  # Make sure you have a compatible driver installed
        driver.get(pdf_url)

        # If you want to open the locally saved PDF, you can use the 'file://' URL:
        # pdf_file_path = 'downloaded.pdf'
        # driver.get('file://' + pdf_file_path)

        # Close the browser after viewing
        input("Press Enter to close the browser...")
        driver.quit()
    else:
        print("No PDF links found on the webpage.")


if __name__ == "__main__":
    download_pdf()