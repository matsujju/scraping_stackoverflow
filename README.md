# Scraping_Stackoverflow
This is a Scrapy project to scrape Questions and Tags from [Stackoverflow](https://stackoverflow.com/questions) and contains files in this repo.

**Disclaimer: This Project is made for educational purpose only. I haven't scraped the whole stackoverflow. If you use this program, use at your own risk, the author won't be liable for your any deeds. Moreover, Stackoverflow do provide it's data in public domain from time to time and you can download it using their API.**

## Extracted Data-
 This Project extracts Questions combined with their title and tags. The extracted data looks like this sample:
 ```
 {
 "title": ["Paste a value in a cell that is \u201cx\u201d columns to the right"],
 "text": ["\r\n                \r\n", "<p>I would like to use the result of a \"match\" querry, to dictate what cell to paste a value (previously copied manually) using relative references in excel.</p>", "\n", "<p>That is, if the \"match\" querry is 3, then I want to paste something 5 cells to the right.</p>", "\n", "<p>If the match query is 4, then I want to paste something 6 cells to the right.</p>", "\n", "<p>I will have already \"copied\" what I need to paste.</p>", "\n", "<p>I will being doing this regularly when updating a schedule.  I need to be able to update multiple lines, by running the macro multiple times.</p>", "\n    "], 
 "tags": ["excel", "vba"]
 }
 ```
 ## Running The Spider locally-
 First create a virtual environment with conda or venv inside a temp folder, then activate it.
```
virtualenv venv

# Windows
venv\Scripts\activate
# Or Linux
source venv/bin/activate

```
Clone the git repo, then install the scrapy with pip
```
git clone https://github.com/matsujju/scraping_stackoverflow.git
cd Desktop/temp_folder/scraping_stackoverflow/        (Here temp_folder is in Desktop...choose your own path if different)
pip install scrapy  (from terminal)
```
You can run a spider using the `scrapy crawl` command, such as
```
$ scrapy crawl questions      (here questions is spider name)
```
If you want to save the scraped data to a file, you can pass the -o option:
```
$ scrapy crawl questions -o data.json
```
