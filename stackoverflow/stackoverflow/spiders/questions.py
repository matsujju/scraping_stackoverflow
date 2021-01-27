import scrapy


class QuestionsSpider(scrapy.Spider):
    name = "questions"
    allowed_domains = ["stackoverflow.com"]
    start_urls = ["https://stackoverflow.com/questions"]

    def parse(self, response):
        questions = response.xpath(
            '//div[@class="summary"]/h3/a'
        )  # extracting the question title link for moving to another page where question text is asked
        for q in questions:
            link = q.xpath(".//@href").get()

            absolute_url = response.urljoin(link)
            yield response.follow(url=absolute_url, callback=self.parse_question)
        next_page = response.xpath(
            "//*[@rel='next']/@href"
        ).extract_first()  # extracting next page link

        absolute_next_page = response.urljoin(next_page)

        if absolute_next_page is not None:
            yield response.follow(url=absolute_next_page, callback=self.parse)

    def parse_question(self, response):
        text = response.xpath(
            "//div[@class='s-prose js-post-body']/child::node()"
        ).extract()  # Questiin text
        title = response.xpath(
            "//*[@id='question-header']/h1/a/text()"
        ).extract()  # Question title
        tags = response.xpath(
            '//*[@id="question"]/div/div[2]/div[2]/div/div/a/text()'
        ).extract()  # Question tags

        yield {
            "text": text,
            "title": title,
            "tags": tags,
            "user-agent": response.request.headers.get("User-Agent").decode(
                "utf-8"
            ),  # look the middleware.py file for more
        }
