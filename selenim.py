# Import necessary libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import csv

# Set up the Chrome browser for web scraping
browser = webdriver.Chrome()
options = webdriver.ChromeOptions()

# Add necessary arguments to the browser options
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-proxy-certificate-handler')
options.add_experimental_option("detach", True) 

# Apply the options to the browser
browser = webdriver.Chrome(options=options)

# Initialize variables
myItem = []
pageN= 10

# Loop through the pages of job listings
for l in range (13):
    try :
        # Access the webpage
        browser.get(f"https://www.indeed.com/jobs?q=amazon&l=New+York%2C+NY&radius=15&start={pageN}")
        src = browser.page_source

        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(src , "html.parser")
        serechR = soup.find('div',{'id','mosaic-provider-jobcards'})
        cards = serechR.select('ul > li .cardOutline')

        # Loop through the job cards on the page
        for i in range(len(cards)):
            # Extract job title and location
            jopTitel = cards[i].select_one('h2')     
            joplocation =cards[i].select_one('.company_location')
            jobsStateDate =cards[i].select_one('[data-testid="myJobsStateDate"]')
            
            # Check if job title and location exist
            if  joplocation is not None and jopTitel is not None :
                item = [jopTitel.text , joplocation.text ]
            
            # Check if job state date exists
            if jobsStateDate is not None :
                item.append(jobsStateDate.text) 
            
            # Append the job details to the list
            myItem.append(item)
        
        # Print the current page number
        print('PN'+str(pageN))
        
        # Move to the next page
        pageN = pageN + 10
    except Exception as e:
        print(f"An error occurred: {e}")
# Close the browser
browser.quit()

# Define the headers for the CSV file
header_list = ['jop title','jop location','Date']

# Write the job details to a CSV file
with open ('D:\Programming\web scraping\indeed\indeedP2.csv','w',encoding='utf-8-sig') as mydata:
    csvfille = csv.writer(mydata)
    csvfille.writerow(header_list)
    csvfille.writerows(myItem)

# Print the total number of jobs scraped
print('Number of Jobs'+str(len(myItem)))

# Print a completion message
print('Job scraping completed successfully.')
