# _Scraping an E-commerce Website Guide_

**Hi there, Welcome to learning logs!**

As part of my ongoing career switch journey to data engineering, I’ve recently been learning about data wrangling, especially I learned about Web Scraping.

**To track my progress and solidify my understanding, I created this project to share what I've learned.**

---
---

# Objective

For this project, I scraped data from **[AliExpress.com](https://best.aliexpress.com/?browser_redirect=true)**

In this guide, I’ll explain the steps I’ve learned to do a web scraping until it can be use, including:

- Scraping the selected website
  
- Parse the scraped data

- Transform the data

---
---

# Workflows

Here's the workflow I followed while building this project:

![scraping-worfklow](https://github.com/Rico-febrian/scraping-ecommerce-website/blob/main/assets/web-scraping-design.png)

---
---

> [!WARNING]
> **BEFORE SCRAPING A WEBSITE, MAKE SURE TO REVIEW ITS TERMS & CONDITIONS!**
>
> **DO NOT USE WEB SCRAPING FOR CRIMINAL ACTIVITIES.**
>
> **ALL INFORMATION FROM WEB SCRAPING IN THIS PROJECT IS ONLY DONE FOR LEARNING PURPOSES!**
>
> **READ THIS BEFORE DO A SCRAPING FOR THIS PROJECT!**
> 
> **[!! CHECK THIS BEFORE SCRAPING !!](https://webscraping.ai/faq/aliexpress-scraping/is-there-a-limit-to-the-amount-of-data-i-can-scrape-from-aliexpress#:~:text=Terms%20of%20Service%3A%20Before%20you,the%20service%20you%20are%20using.)**

---
---

**Alright, let's started!**

**Before we begin scraping the web, take a look at the requirements and preparation below:**

# Requirements

- Programming Language:
    - Python

- Browser
  - Microsoft Edge (for locate the selector)

- Python Libray:
    - Playwright
    - Beautifulsoup4
    - Pandas

 > [!NOTE]
 > **Make sure these tools and packages are installed and set up before starting the implementation!**.
      
---

# Preparation

- ## Setup project environment

  Create and activate python environment to isolate project dependencies.
  
  ```
  python -m venv your_project_name         
  source your_project_name/bin/activate    # On Windows: your_project_name\Scripts\activate
  ```

- ## Install _requirements.txt_ in the created environment
  
  ```
  pip install -r requirements.txt
  ```
  
  **Note: You can install libraries as needed while developing the code. However, once complete, make sure to generate a _requirements.txt_ file listing all dependencies**.

---

# Building the Scraper

This script is designed to extract and save the HTML content from a specified website. Here's the step-by-step process I followed to develop the script:

- ## Check the Website and Choose the Section

  The first step is to visit the selected website and identify the specific section you want to scrape.
  
  For this project, I decided to scrape the items displayed in the "More to Love" section on the homepage.
  
  ![homepage](https://github.com/Rico-febrian/scraping-ecommerce-website/blob/main/assets/homepage.png)

---

- ## Define the Scraping Workflow

  To make the scraping process easier to understand, I designed a workflow that breaks down each step of what happens when the scraping script runs. Here's the workflow I designed:
  
  - Access the website, wait the content load
  
  - Click `Ship to` form
  
  - Click to input location field
  
  - Fill it with 'United States'
  
  - Click the 'United States' location
  
  - Click the save button, wait until content load
  
  - Scroll up to the main contents
  
  - Click view more until the end of the page
  
  **This workflow will guide the creation of the scraping logic and make the process easier.**

---

- ## Find and Set up the needs selector

> [!IMPORTANT]
> In this project, I located the selectors using the Microsoft Edge browser.
> _**If you use a different browser, the selectors might vary because the website isn’t static, and you may need to adjust them accordingly**_

  Based on the workflow, I identify the specific selectors required for the scraping process.
    
  Here are the selectors I used:  
  
  - ### ship_to
  
    This selector is used to locate the form that allows changing the shipping location.

    ![ship_to_selector](https://github.com/Rico-febrian/scraping-ecommerce-website/blob/main/assets/ship_to_selector.png)
  
  - ### form_content
  
    This selector is used to locate the location input list.

    ![form_content_selector](https://github.com/Rico-febrian/scraping-ecommerce-website/blob/main/assets/form_content_selector.png)
  
  - ### fill_input
  
    This selector is used to locate the input field for selecting a location. In this project, the items will be retrieved from the "United States".

    ![fill_input_selector](https://github.com/Rico-febrian/scraping-ecommerce-website/blob/main/assets/input_selector.png)
   
  - ### usa_input 
  
    This selector is used to locate "United States" from the country list.

    ![usa_input_selector](https://github.com/Rico-febrian/scraping-ecommerce-website/blob/main/assets/input_usa_selector.png)
  
  - ### save_button
  
    This selector is used to locate the save button in shipping location form.

    ![save_button_selector](https://github.com/Rico-febrian/scraping-ecommerce-website/blob/main/assets/save_button_selector.png)
  
  - ### all_items
  
    This selector is used to locate all the main content/items that need to be scraped.

     ![items_selector](https://github.com/Rico-febrian/scraping-ecommerce-website/blob/main/assets/items_selector.png)
  
  - ### next_page_button 
  
    This selector is used to locate the "_Next Page_" or "_View More Items_" button in the main content section.

    ![next_page_selector](https://github.com/Rico-febrian/scraping-ecommerce-website/blob/main/assets/next_page_selector.png)
  

  **All these selectors are utilized in the scraping script to navigate and extract the required data.**

---

- ## Create Scraping Logic

To create scraping scripts, I use async Playwright because it allows performing multiple tasks (such as page navigation, element extraction, and button clicking) concurrently, making it faster and more efficient.

  - ### Setup the Main function

    - Create an async function to scrapes data from the selected website and saved the HTML content.

        ```
        async def your_main_function_name():
        
          try:
        
                ....... MAIN CODE ......
                ....... MAIN CODE ......
                ....... MAIN CODE ......
        
          # Error handling
          except PlaywrightTimeoutError:
            print("")
          except Exception as e:
              print(f"")
          finally:
               # Close the browser if it was opened
              if browser:
                  await browser.close()
        ```
  
  - ### Setup the Browser
    
    - In main function, setup the config to launch the browser. 

      ```
        try:
      
            # Set the playwright context manager
            async with async_playwright() as p:
    
                # Launch the Chromium browser in headless mode (set headless=True to run in background)
                browser = await p.chromium.launch(headless=False)  
    
                # Open a new page/tab in the browser
                page = await browser.new_page()

                ....... MAIN CODE ......  
      ```

>[!NOTE]
>Playwright supports multiple browsers, including Chrome (via Chromium), Edge, and Firefox.
>You can choose the one that suits your needs by changing _**p.chromium**_ to _**p.firefox**_ or _**p.webkit**_.

  - ### Setup the Website
  
    - Once the browser is set up, configure it to access and load the selected website.

      ```
        try:
      
            # Set the url from selected website 
            website_url = 'https://selected_website.com'
      
            # Access the web page and wait until it is fully loaded
            await page.goto(url, wait_until='networkidle', timeout=60000)

            ....... MAIN CODE ...... 
      ```

  - ### Setup the Selector

    - Define the required selectors based on the scraping workflow created earlier.

      ```
        try:
      
            # Configure the selector to change the location
            ship_to_selector =  Identify elements by XPath, CSS selectors, or text.

            # Set form content selector to fill the location input 
            form_content_selector =  Identify elements by XPath, CSS selectors, or text.

            # Set the input locator to fill the selected location. In this project, 'USA' is selected
            fill_input =  Identify elements by XPath, CSS selectors, or text.

            # UNTIL THE LAST SELECTOR
      
            ....... MAIN CODE ...... 
      ```

  - ### Create the Main Logic

    - After defining the selectors, you can create the main logic based on the scraping workflow design.
      Take a look at my full script to see how the main logic follows the designed workflow: [full-script](https://github.com/Rico-febrian/scraping-ecommerce-website/blob/main/scrape.py)
  
  - ### Saved the HTML content

    - Save the scraped HTML content to a file

      ```
        try:
            ....... MAIN CODE ......
            ....... MAIN CODE ......

            html_content = await page.content()
            with open('DIRECTORY_TO_SAVE_THE_SCRAPED_OUTPUT/SCRAPED_OUTPUT_NAME.html', 'w', encoding='utf-8') as file:
              file.write(html_content)
      
      ``` 

  - ### Run the Script
  
    - To execute the script, run the following command in your terminal: 

      ```
      python your_script_name.py
      ```

  - ### Verify the Scraped Output
  
    - Check the output directory specified in your code to ensure the data has been scraped correctly.
      Check here to see the scraped output: [scraped-output](https://github.com/Rico-febrian/scraping-ecommerce-website/tree/main/scraping_output) 
---
---

# Parsing the Scraped Data

After successfully scraping the HTML content, the next step is to parse it so the data becomes structured and readable.

- ## Locate and Identify the HTML Element

  - Identify the HTML elements (e.g., tags, attributes, and classes) that contain the information you want to extract. Here are the HTML elements I parsed:

    - Get all listing information

      ![get_listing_element](https://github.com/Rico-febrian/scraping-ecommerce-website/blob/main/assets/get_all_listing.png)
      
    - Get item title
      
      ![get_title_element](https://github.com/Rico-febrian/scraping-ecommerce-website/blob/main/assets/get_title.png)

    - Get item price

      ![get_price_element](https://github.com/Rico-febrian/scraping-ecommerce-website/blob/main/assets/get_price.png)

    - Get item rating
      
      ![get_rating_element](https://github.com/Rico-febrian/scraping-ecommerce-website/blob/main/assets/get_rating.png)

    - Get item url
      
      ![get_url_element](https://github.com/Rico-febrian/scraping-ecommerce-website/blob/main/assets/get_link.png)
  
- ## Parse the selected element into the script

  - Based on the identified elements, you can parse the selected element using BeautifoulSoup to locate and extract the information.
  
    ```
    # To retrieve all instances of a specific element in the HTML document
    get_all_items = soup.find_all('tag_name', class_='class_name')
    
    # Or if you want to find a specific item
    get_title = item.find('tag_name', class_='class_name').text
    
    ```
    Check here to see the completed parsing script: [parse-script]()

- ## Save and run the script

  - Convert the parsed HTML data into a DataFrame and save it into a CSV file using Pandas.

  - Then run the parsing script. 

    ```
    python your_script_name.py
    ```

- ## Verify the parsed output

  - Check the directory specified in your script to confirm the data was parsed and saved correctly.
    Check here to see the parsed output: [parsed-output](https://github.com/Rico-febrian/scraping-ecommerce-website/tree/main/parsed_output) 

---
---

# Transforming the Data

The final step is to clean and transform the parsed data based on your needs or business requirements. Here are the transformations I performed using Pandas:

- `title` column: Convert values to lowercase.

- `price` column:

  - Remove the '$' character
  - Cast the data type to numeric
  
- Create a new column named `price_currency` with the value 'USD'.

- Rename columns:

  - `title` → `listing_title`
  - `url` → `source_url`

- Reorder columns: Arrange columns as follows: `listing_title`, `price`, `price_currency`, `rating`, `source_url`.

To see how I transformed the data based on the requirements above, check here: [transform-data](https://github.com/Rico-febrian/scraping-ecommerce-website/tree/main/transformed_output)

---
---

# Final Result

- ## Scraped Output (HTML file)

  ![scraped-output](https://github.com/Rico-febrian/scraping-ecommerce-website/blob/main/assets/scraped_output.png)
  
- ## Parsed Output (CSV)

  ![parsed-output](https://github.com/Rico-febrian/scraping-ecommerce-website/blob/main/assets/parsed_output.png)
  
- ## Transformed Output (CSV)

  ![transformed-output](https://github.com/Rico-febrian/scraping-ecommerce-website/blob/main/assets/transformed_output.png)

---
---

# Conclusion

Well, you’ve reached the end of this guide. In summary, I’ve shared my learning journey in data engineering, with a focus on web scraping.

**Key takeaways include:**

- Always review the terms and conditions before starting any web scraping activities.

- Define the scraping workflow beforehand to ensure a clear and efficient process.

- Learn how to implement the design into code effectively.

Thank you for joining me on this learning experience! I hope you’ve gained valuable insights to support your own data engineering journey. 
If you have any questions or need further information, feel free to reach out. I welcome your feedback and suggestions.

**You can connect with me on:** 

- [My LinkedIn](www.linkedin.com/in/ricofebrian)
- [My Medium](https://medium.com/@ricofebrian731)