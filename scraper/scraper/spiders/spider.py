# scrapy startproject projectname
# scrapy crawl name(posts here)
import scrapy


class PostsSpider(scrapy.Spider):
    name = "posts"
    start_urls = [
        'https://blog.scrapinghub.com/page/1/',
        #'https://blog.scrapinghub.com/page/2/'
    ]

    """def parse(self, response):
        page = response.url.split('/')[-1]
        filename = 'posts-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)"""

    def parse(self, response):
        for post in response.css('div.post-item'):
            yield{
                'title': post.css('.post-header h2 a::text')[0].get(),
                'date': post.css('.post-header  a::text')[1].get(),
                'author': post.css('.post-header  a::text')[2].get()
            }
        next_page = response.css('a.next-posts-link::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)



#scrapy shell url to open in shell
#now select anything
#response.css('title') --for title .get() got just the element  title::text to get text  -- fetches in list getall() for all
#'.classname' for class
# select inside the class by .classname{space}tag
#.re(r') for regular expression
#.xpath for xml path
# -o filename.json/xml/csv