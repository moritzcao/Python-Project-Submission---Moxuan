import selenium.common.exceptions
from selenium import webdriver

# Initiate a webdriver
driver = webdriver.Chrome()

# Create an empty list to contain rows scrapped from website
lines = []

for page in range(0, 20):
    # Directly get url so that we can skip clicking "next page" button
    if page == 0:
        driver.get(f'https://www.imdb.com/search/title/?groups=top_1000&view=advanced')
    else:
        driver.get(f'https://www.imdb.com/search/title/?groups=top_1000&start={(page*50)+1}&ref_=adv_nxt')

    try:
        # Find the "blocks" on the page, which are single cells that contains movie info
        movie_blocks = driver.find_elements_by_xpath('//div[@class="lister-item mode-advanced"]')
        print(f'Scraping info from page {page+1}')

    except selenium.common.exceptions.NoSuchElementException:
        # Sometimes the page fails to load. Catch the exception and skip scraping this page
        print(f'Failed to load page {page+1}')
        continue

    for movie_block in movie_blocks:
        # Find information for each movie based on element's class/tag names
        header = movie_block.find_element_by_class_name('lister-item-header')
        rank = header.find_element_by_class_name('lister-item-index').text.replace('.', '')
        title = header.find_element_by_tag_name('a').text
        link = header.find_element_by_tag_name('a').get_attribute('href')
        year = header.find_element_by_class_name('lister-item-year').text.replace('(', '').replace(')', '')
        genre = movie_block.find_element_by_class_name('genre').text
        description = movie_block.find_elements_by_class_name('text-muted')[2].text

        # Append scrapped row into the list
        line = '\t'.join([rank, title, link, year, genre, description])
        lines.append(line)

# Write results into an .txt file. Uses \t to separate columns in order to make Pandas easier to read it as CSV
with open('IMDB_Movies.txt', 'w', encoding='utf-8', errors='ignore') as f:
    f.write('rank\ttitle\tlink\tyear\tgenre\tdescription\n')
    for line in lines:
        f.write(line + '\n')
