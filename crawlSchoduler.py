from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from googlescholar.spiders.googlescholerSpider import ScholarSpider
from scrapy.crawler import CrawlerRunner


def crawl_job():
    print('Started Crawling')
    settings = get_project_settings()
    runner = CrawlerRunner(settings)
    return runner.crawl(ScholarSpider)


def schedule_next_crawl(null, schedule_time):
    reactor.callLater(schedule_time, crawl)


def crawl():
    d = crawl_job()
    d.addCallback(schedule_next_crawl, 3600)
    d.addErrback(catch_error)


def catch_error(failure):
    print(failure.value)

crawl()
reactor.run()
