# Web-Scraping-Project-Job-Data-Collection
This project involves using Python to scrape job data from the Indeed website
The script navigates through multiple pages of job listings for Amazon in New York, NY, and collects information about each job. The collected data is then written to a CSV file.
The script uses Selenium to navigate the Indeed website and BeautifulSoup to parse the HTML of the web pages. It iterates over 13 pages of job listings, with each page containing about 14 jobs. For each job, it collects the job title, job location, and the date the job was posted (if available). This data is stored in a list of lists (myItem), with each inner list representing a job and its associated data.

The script keeps track of the number of jobs for which it was able to collect the date (nOfDataStat). After collecting the data, the script writes it to a CSV file (indeedP2.csv) located in the specified directory. The headers of the CSV file are ‘jop title’, ‘jop location’, and ‘Date’.

The script prints the page number it’s currently scraping to keep track of its progress. Once it has finished scraping all the pages and writing the data to the CSV file, it prints the total number of jobs for which it collected the date and a ‘done’ message to indicate successful completion of the script.

This project provides a practical application of web scraping to collect valuable data for job market analysis. It can be modified to scrape job data for different companies, locations, or job types by changing the URL and the elements being selected.
