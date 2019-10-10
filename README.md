NewsPaper is Python project that is used to scrapy key elements of blog posts (author, text, publication date, and keywords). 
It is especially useful for find keywords in the text for SEO or marketing.

Requirements:
- Python 3 (I tested with version 3.6)
- Pythons library newsPaper3K and nltk
- Scrapy (version 1.7 is used in the program)

Instructions:
- In the csvInput folder, remember the csv file with internet URLs of the articles you want to process (an example of an input 
  file is inputFile.csv in the csvInput folder)
- Open the terminal, go to newsPaper (the main folder)
- Run command "scrapy crawl news -o <name_output_file_what_you_want.csv>"(or other extensions: json, xlm)
