import pandas as pd

# Transform the parsed data
def transform_data(parsed_data_path, output_path):
              
    """
    Function to read, clean and transform the parsed data, then export it to a CSV file.
    
    Parameters:
        - parsed_data_path (str): The path where the parsed data is saved.
        - output_path (str): The path where the transformed data will be saved as a CSV file.
    
    """
    
    # Read the parsed data file
    with open(file = parsed_data_path, mode = 'r') as raw_scraped_data:
        scraped_data = pd.read_csv(raw_scraped_data)
        
    # Transform "title" column
    # Convert the values to a lowercase
    scraped_data['title'] = scraped_data['title'].str.lower()

    # Transform "price" column
    # Remove the '$' character and generate a new column named 'price_currency'"
    scraped_data['price'] = scraped_data['price'].str.replace('$', '')

    # Cast the data type to a numeric
    scraped_data['price'] = scraped_data['price'].astype(float)

    # Generate new column to store a price currency 
    scraped_data['price_currency'] = 'USD'

    # Rename the columns
    # Specify the column to be renamed from the product data
    rename_cols = {
        'title' : 'listing_title',
        'url' : 'source_url'
    }

    # Update the data
    scraped_data = scraped_data.rename(columns=rename_cols)
    
    # Mapping the columns
    # Define the order of columns to be mapped
    mapping_cols = [
        'listing_title',
        'price',
        'price_currency',
        'rating',
        'source_url'
    ]

    # Update the data
    scraped_data = scraped_data[mapping_cols]
    
    # Export the transformed scraped data to a CSV
    scraped_data.to_csv(output_path, index=False)
    
    
# Run the function
transform_data(parsed_data_path="parsed_output/parsed_data.csv",
               output_path="transformed_output/transformed_data.csv")