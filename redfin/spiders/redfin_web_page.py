from w3lib.html import remove_tags
from web_poet.pages import ItemWebPage


class RedfinPage(ItemWebPage):

    @property
    def address(self):
        add = self.xpath('//span[@data-rf-test-id="abp-homeinfo-homeaddress"]')
        l_xp = './/span/span[@data-rf-test-id="abp-cityStateZip"]/span/text()'
        pc_xp = './/span/span[@data-rf-test-id="abp-cityStateZip"]/span[@class="postal-code"]/text()'
        r_xp = './/span/span[@data-rf-test-id="abp-cityStateZip"]/span[@class="region"]/text()'
        s_xp = './/span/span/text()'
        _address = {
            'locality': add.xpath(l_xp).get(),
            'postal_code': add.xpath(pc_xp).get(),
            'region': add.xpath(r_xp).get(),
            'street': add.xpath(s_xp).get()
        }
        if _address['street'] is None:
            add = self.xpath('//h1[@data-rf-test-id="abp-homeinfo-homeaddress"]')
            city_state_zip = add.xpath('.//div[@data-rf-test-id="abp-cityStateZip"]/text()').get()
            region, locality_zip = city_state_zip.split(',')
            locality, zip_code = locality_zip.strip().split()
            _address = {
                'locality': locality,
                'postal_code': zip_code,
                'region': region,
                'street': add.xpath('.//div/span/text()').get()
            }
        return _address

    @property
    def _agent_info(self):
        return self.xpath('//div[@class="agent-info-item"]/div/span')

    @property
    def agent_company(self):
        _ac = self._agent_info.xpath('.//span').get()
        try:
            return remove_tags(_ac).replace('•', '')
        except:
            return _ac

    @property
    def agent_name(self):
        return self._agent_info.xpath('.//a/text()').get()

    @property
    def bath(self):
        return self.xpath(
            '//div[@data-rf-test-id="abp-baths"]/div[@class="statsValue"]/text()'
        ).get()

    @property
    def beds(self):
        return self.xpath(
            '//div[@data-rf-test-id="abp-beds"]/div[@class="statsValue"]/text()'
        ).get()

    @property
    def brokerage_compensation(self):
        return self.xpath(
            '//span[text()="Buyer\'s Brokerage Compensation"]/following-sibling::span/text()'
        ).get()

    @property
    def build_date(self):
        return self.xpath(
            '//span[@data-rf-test-id="abp-yearBuilt"]/span[@class="value"]/text()'
        ).get()

    @property
    def description(self):
        return self.xpath(
            '//div[@data-rf-test-id="listingRemarks"]/p/span/text()'
        ).get()

    @property
    def est_mo_payment(self):
        return self.xpath(
            '//span[text()="Est. Mo. Payment"]/following-sibling::span/text()'
        ).get()

    @property
    def estimated_payment(self):
        calc = self.xpath('//div[@data-rf-test-name="mc-summary"]/div')
        monthly = calc.xpath('.//p[contains(@class, "title")]/text()').get()
        _ep = {'monthly': monthly}
        for row in calc.xpath('.//div[contains(@class, "Row")]'):
            key = row.xpath('.//span/div/span/text()').get()
            value = row.xpath('.//span[2]/text()').get()
            _ep[key] = value
        return _ep

    @property
    def home_facts(self):
        hf = {}
        s = self.xpath('//div[contains(@class, "keyDetails--HomeFacts")]/following-sibling::div')
        for kvp in s.xpath('.//div[contains(@class, "keyDetail")]'):
            key = kvp.xpath('.//span/text()').get()
            value = kvp.xpath('.//span[2]/text()').get()
            hf[key] = value
        return hf

    @property
    def lot_size(self):
        return self.xpath(
            '//span[@data-rf-test-id="abp-lotSize"]/span[@class="value"]/text()'
        ).get()

    @property
    def offer_stats(self):
        _os = {}
        div_os = self.xpath('//div[@class="offer-stats"]')
        for td in div_os.xpath('.//td'):
            title = td.xpath('.//span/text()').get()
            value = td.xpath('.//span[2]/text()').get()
            _os[title] = value
        return _os

    @property
    def price(self):
        return self.xpath(
            '//div[@data-rf-test-id="abp-price"]/div/div/span[2]/text()'
        ).get()

    @property
    def price_sqft(self):
        return self.xpath(
            '//div[@data-rf-test-id="abp-sqFt"]/span/div/text()'
        ).get()

    @property
    def property_details(self):
        _pd = {}
        div_pd = self.xpath('//div[@data-rf-test-id="propertyDetails"]')
        div_scc = div_pd.xpath('.//div[contains(@class, "sectionContentContainer")]')
        for sgt, sgc in zip(
            div_scc.xpath('.//div[@class="super-group-title"]'),
            div_scc.xpath('.//div[@class="super-group-content"]')
        ):
            title = sgt.xpath('.//text()').get()
            _pd[title] = {}
            for ag in sgc.xpath('.//div[@class="amenity-group"]'):
                amenity_group_title = remove_tags(ag.xpath('.//h3').get())
                amenities = [remove_tags(a) for a in ag.xpath('.//li').getall()]
                _pd[title][amenity_group_title] = amenities
        return _pd

    @property
    def public_facts(self):
        _pf = {}
        div_pr = self.xpath('//div[@data-rf-test-id="publicRecords"]')
        for row in div_pr.xpath('.//div[@class="table-row"]'):
            key = row.xpath('.//span/text()').get()
            value = row.xpath('./div/text()').get()
            _pf[key] = value
        return _pf

    @property
    def scores(self):
        _scores = {}
        div_ws = self.xpath('//div[@class="walk-score"]')
        for name, value in zip(
            div_ws.xpath('.//div[contains(@class, "walkscore-trademark")]/text()').getall(),
            div_ws.xpath('.//span[contains(@class, "value")]/text()').getall()
        ):
            _scores[name] = value
        return _scores

    @property
    def sq_ft(self):
        return self.xpath(
            '//div[@data-rf-test-id="abp-sqFt"]/span/span/text()'
        ).get()

    @property
    def status(self):
        return self.xpath(
            '//span[text()="Status"]/following-sibling::span/text()'
        ).get()

    @property
    def time_on_redfin(self):
        return self.xpath(
            '//span[text()="Time on Redfin"]/following-sibling::span/text()'
        ).get()

    def to_item(self):
        yield {
            'address': self.address,
            'agent_name': self.agent_name,
            'agent_company': self.agent_company,
            'bath': self.bath,
            'beds': self.beds,
            'brokerage_compensation': self.brokerage_compensation,
            'build_date': self.build_date,
            'description': self.description,
            'estimated_payment': self.estimated_payment,
            'est_mo_payment': self.est_mo_payment,
            'home_facts': self.home_facts,
            'lot_size': self.lot_size,
            'offer_stats': self.offer_stats,
            'price': self.price,
            'price_sqft': self.price_sqft,
            'property_details': self.property_details,
            'public_facts': self.public_facts,
            'scores': self.scores,
            'sq_ft': self.sq_ft,
            'status': self.status,
            'time_on_redfin': self.time_on_redfin
        }
