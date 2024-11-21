import pandas as pd
from bs4 import BeautifulSoup

# Transform the scraped data
def parse_html(html_path, output_path):
    
    """
    
    Function to read and parse the scraped data and export it to a CSV file.

    Parameters:
        - html_path (str): The path where the scraped HTML data is saved.
        - output_path (str): The path where the parsed data will be saved as a CSV file.
    
    """
    
    try:
        
        # Read and create beautifulsoup object for parsing the scraped HTML data
        with open(file = html_path, mode = 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
        
        # Get all listings from scraped HTML data
        get_item_list = soup.find_all('div', class_= 'recommend-card--card-wrap--2jjBf6S')

        # Define an empty list to store the extracted data for each listing
        full_data = []

        # Iterate each item through all item listing
        for item in get_item_list:
            
            # Get title of the listing
            get_title = item.find('div', attrs={'title' : True}).text
            
            # Get price of the listing
            get_price = item.find('span', class_= 'rc-modules--price--1NNLjth').text
            
            # Get rating of the listing
            get_rating = item.find('div', class_= 'rc-modules--stars--o9mzAea').get('title')
            
            # Get url of the listing
            get_url = item.find('a', class_= 'recommend-card--recommend-card--36CHUyg').get('href')
            
            # Map the extracted data into a dictionary
            data = {
                'title' : get_title,
                'price' : get_price,
                'rating' : get_rating,
                'url' : get_url
            }
            
            # Append the mapped data to the full data list
            full_data.append(data)
        
    except Exception as e:
        print(f'Error: {e}')
    
    # Convert scraped data into a dataframe
    scrape_data = pd.DataFrame(full_data)
    
    # Export to CSV
    scrape_data.to_csv(output_path, index=False)
    
# Run the function
parse_html(html_path="scraping_output/ali-express-scrape-us.html",
           output_path="parsed_output/parsed_data.csv")