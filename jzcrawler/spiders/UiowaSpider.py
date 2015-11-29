#import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from jzcrawler.items import JzcrawlerItem

class UiowaSpider(CrawlSpider):
    name = "UiowaSpider"
    #allowed_domains = ["uiowa.edu", "uiortho.com"]
    allowed_domains = ["uiowa.edu"]
    start_urls = ["http://www.uiowa.edu/"]
    rules = (
        #Rule(SgmlLinkExtractor(allow=('.*.uiowa.edu', ), deny=('_ticket=', 'infohawk.uiowa.edu:80/F/', '.*.lib.uiowa.edu', 'utm_source=', 'utm_campaign=', 'utm_medium=', )),
        #GraduateCollege Rule(SgmlLinkExtractor(allow=('http://www.grad.uiowa.edu', ), deny=('_ticket=', 'infohawk.uiowa.edu:80/F/', '.*.lib.uiowa.edu', 'utm_source=', 'utm_campaign=', 'utm_medium=', 'http://tippie.uiowa.edu/fulltimemba/calendar/', 'calendar', )),
        #UniversityCollege Rule(SgmlLinkExtractor(allow=('http://uc.uiowa.edu', ), deny=('_ticket=', 'infohawk.uiowa.edu:80/F/', '.*.lib.uiowa.edu', 'utm_source=', 'utm_campaign=', 'utm_medium=', 'http://tippie.uiowa.edu/fulltimemba/calendar/', 'calendar', )),
        #ContinuingEducation Rule(SgmlLinkExtractor(allow=('http://www.uiowa.edu/dce/', 'http://distance.uiowa.edu/', ), deny=('_ticket=', 'infohawk.uiowa.edu:80/F/', '.*.lib.uiowa.edu', 'utm_source=', 'utm_campaign=', 'utm_medium=', 'http://tippie.uiowa.edu/fulltimemba/calendar/', 'calendar', )),
        #Tippie College of Business Rule(SgmlLinkExtractor(allow=('http://tippie.uiowa.edu/', ), deny=('_ticket=', 'infohawk.uiowa.edu:80/F/', '.*.lib.uiowa.edu', 'utm_source=', 'utm_campaign=', 'utm_medium=', 'http://tippie.uiowa.edu/fulltimemba/calendar/', 'calendar', )),
        #Carver College of Medicine Rule(SgmlLinkExtractor(allow=('http://www.medicine.uiowa.edu/', 'http://www.anesth.uiowa.edu/', 'http://www.physiology.uiowa.edu/', 'http://www.uiortho.com/', ), deny=('_ticket=', 'infohawk.uiowa.edu:80/F/', '.*.lib.uiowa.edu', 'utm_source=', 'utm_campaign=', 'utm_medium=', 'http://tippie.uiowa.edu/fulltimemba/calendar/', 'http://www.tippie.uiowa.edu/fulltimemba/calendar/', 'calendar', 'http://www.anesth.uiowa.edu/Default.aspx?ctl=Login', 'login', 'Login', )),
        #College of Dentistry Rule(SgmlLinkExtractor(allow=('http://www.dentistry.uiowa.edu/', 'https://www.dentistry.uiowa.edu/', ), deny=('_ticket=', 'infohawk.uiowa.edu:80/F/', '.*.lib.uiowa.edu', 'utm_source=', 'utm_campaign=', 'utm_medium=', 'http://tippie.uiowa.edu/fulltimemba/calendar/', 'calendar', 'http://www.anesth.uiowa.edu/Default.aspx?ctl=Login', 'login', 'Login', 'http://www.dentistry.uiowa.edu/events/', 'https://www.dentistry.uiowa.edu/events/', )),
        #College of Liberal Arts and Sciences Rule(SgmlLinkExtractor(allow=('http://clas.uiowa.edu/', 'http://www.clas.uiowa.edu/', 'http://www.art.uiowa.edu/', 'http://www.biology.uiowa.edu/', 'http://www.chem.uiowa.edu/', 'https://www.cs.uiowa.edu/', 'http://www.cs.uiowa.edu/', 'http://dance.uiowa.edu/', 'http://www.dance.uiowa.edu/', 'http://deltacenter.uiowa.edu/', 'http://www.deltacenter.uiowa.edu/', 'http://english.uiowa.edu/', 'http://www.english.uiowa.edu/', 'http://math.uiowa.edu/', 'http://www.math.uiowa.edu/', 'http://music.uiowa.edu/', 'http://www.music.uiowa.edu/', 'http://www.ostc.uiowa.edu/', 'http://dpa.uiowa.edu/', 'http://www.dpa.uiowa.edu/', 'http://www.physics.uiowa.edu/', 'http://www.psychology.uiowa.edu/', 'http://www.stat.uiowa.edu/', 'http://theatre.uiowa.edu/', 'http://www.theatre.uiowa.edu/', 'http://writersworkshop.uiowa.edu/', 'http://www.writersworkshop.uiowa.edu/', ), deny=('_ticket=', 'infohawk.uiowa.edu:80/F/', '.*.lib.uiowa.edu', 'utm_source=', 'utm_campaign=', 'utm_medium=', 'http://tippie.uiowa.edu/fulltimemba/calendar/', 'calendar', 'http://www.anesth.uiowa.edu/Default.aspx?ctl=Login', 'login', 'Login', 'http://www.dentistry.uiowa.edu/events/', 'https://www.dentistry.uiowa.edu/events/', )),
        #College of Education Rule(SgmlLinkExtractor(allow=('http://education.uiowa.edu/', 'http://www.education.uiowa.edu/', ), deny=('_ticket=', 'infohawk.uiowa.edu:80/F/', '.*.lib.uiowa.edu', 'utm_source=', 'utm_campaign=', 'utm_medium=', 'http://tippie.uiowa.edu/fulltimemba/calendar/', 'calendar', 'http://www.anesth.uiowa.edu/Default.aspx?ctl=Login', 'login', 'Login', 'http://www.dentistry.uiowa.edu/events/', 'https://www.dentistry.uiowa.edu/events/', )),
        #College of Engineering Rule(SgmlLinkExtractor(allow=('http://engineering.uiowa.edu/', 'http://www.engineering.uiowa.edu/', ), deny=('_ticket=', 'infohawk.uiowa.edu:80/F/', '.*.lib.uiowa.edu', 'utm_source=', 'utm_campaign=', 'utm_medium=', 'http://tippie.uiowa.edu/fulltimemba/calendar/', 'calendar', 'http://www.anesth.uiowa.edu/Default.aspx?ctl=Login', 'login', 'Login', 'http://www.dentistry.uiowa.edu/events/', 'https://www.dentistry.uiowa.edu/events/', )),
        #College of Law Rule(SgmlLinkExtractor(allow=('http://law.uiowa.edu/', 'http://www.law.uiowa.edu/', ), deny=('_ticket=', 'infohawk.uiowa.edu:80/F/', '.*.lib.uiowa.edu', 'utm_source=', 'utm_campaign=', 'utm_medium=', 'http://tippie.uiowa.edu/fulltimemba/calendar/', 'calendar', 'http://www.anesth.uiowa.edu/Default.aspx?ctl=Login', 'login', 'Login', 'http://www.dentistry.uiowa.edu/events/', 'https://www.dentistry.uiowa.edu/events/', )),
        #College of Nursing Rule(SgmlLinkExtractor(allow=('http://nursing.uiowa.edu/', 'http://www.nursing.uiowa.edu/', ), deny=('_ticket=', 'infohawk.uiowa.edu:80/F/', '.*.lib.uiowa.edu', 'utm_source=', 'utm_campaign=', 'utm_medium=', 'http://tippie.uiowa.edu/fulltimemba/calendar/', 'calendar', 'http://www.anesth.uiowa.edu/Default.aspx?ctl=Login', 'login', 'Login', 'http://www.dentistry.uiowa.edu/events/', 'https://www.dentistry.uiowa.edu/events/', )),
        #College of Pharmacy Rule(SgmlLinkExtractor(allow=('http://pharmacy.uiowa.edu/', 'http://www.pharmacy.uiowa.edu/', ), deny=('_ticket=', 'infohawk.uiowa.edu:80/F/', '.*.lib.uiowa.edu', 'utm_source=', 'utm_campaign=', 'utm_medium=', 'http://tippie.uiowa.edu/fulltimemba/calendar/', 'calendar', 'http://www.anesth.uiowa.edu/Default.aspx?ctl=Login', 'login', 'Login', 'http://www.dentistry.uiowa.edu/events/', 'https://www.dentistry.uiowa.edu/events/', )),
        #College of Public Health Rule(SgmlLinkExtractor(allow=('http://public-health.uiowa.edu/', 'http://www.public-health.uiowa.edu/', ), deny=('_ticket=', 'infohawk.uiowa.edu:80/F/', '.*.lib.uiowa.edu', 'utm_source=', 'utm_campaign=', 'utm_medium=', 'http://tippie.uiowa.edu/fulltimemba/calendar/', 'calendar', 'http://www.anesth.uiowa.edu/Default.aspx?ctl=Login', 'login', 'Login', 'http://www.dentistry.uiowa.edu/events/', 'https://www.dentistry.uiowa.edu/events/', )),
             Rule(SgmlLinkExtractor(allow=('http://www.uiowa.edu/', 'http://uiowa.edu/', ), deny=('_ticket=', 'infohawk.uiowa.edu:80/F/', '.*.lib.uiowa.edu', 'utm_source=', 'utm_campaign=', 'utm_medium=', 'http://tippie.uiowa.edu/fulltimemba/calendar/', 'calendar', 'http://www.anesth.uiowa.edu/Default.aspx?ctl=Login', 'login', 'Login', 'http://www.dentistry.uiowa.edu/events/', 'https://www.dentistry.uiowa.edu/events/', )),
             callback="parse_items",
             follow=True),
             #follow=False),
    )

    def parse_items(self, response):
        selector = Selector(response)
        anchorItems = selector.xpath('//a/@href')
        items = []
        for anchorItem in anchorItems:
            aItem = JzcrawlerItem()
            aItem["depth"] = response.meta["depth"]
            aItem["title"] = selector.xpath('//title/text()').extract()
            aItem["fromUrl"] = response.url
            aItem["toUrl"] = anchorItem.extract()
            items.append(aItem)
        return(items)
