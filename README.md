# Indeed Job Scraper

This Python script is a web scraper that extracts job listings from Indeed.com.

## Libraries Used

- Selenium: For browser automation
- BeautifulSoup: For parsing HTML
- CSV: For writing the data to a CSV file

## How It Works

1. The script sets up a Chrome browser instance for web scraping and adds necessary arguments to the browser options.
2. It initializes some variables and then loops through the pages of job listings on Indeed.com.
3. For each page, it accesses the webpage, gets the page source, and parses it with BeautifulSoup.
4. It then finds the job cards on the page and loops through them.
5. For each job card, it extracts the job title, location, and state date (if they exist) and appends the job details to a list.
6. After going through all the pages, it closes the browser.
7. Finally, it writes the job details to a CSV file and prints the total number of jobs scraped and a completion message.

## Output

The output is a CSV file with the following headers:
- Job Title
- Job Location
- Date

The file is saved in the 'D:\Programming\web scraping\indeed' directory with the name 'indeedP2.csv'.

