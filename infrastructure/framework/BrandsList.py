class BrandsList(object):

	def __init__(self, brand):
		self.brand = brand
		print("brand .self is " + brand)

	# Todo: Insert all NewForex brands from : https://docs.google.com/spreadsheets/d/1JPuCt2KVvF7WdggVgO1DysmfWfxtJaglX42iR74bvIM/edit#gid=0
	def get_brand_url(self):

		if self.brand == "newforexqa2":
			return {"crm": "https://newforexqa2.ptscrm.com/v2", "ca": "https://newforexqa2.pandats.com/"}

		if self.brand == "newforexstage2":
			return {"crm": "https://newforexstage2.ptscrm.com/v2", "ca": "https://newforexstage2.pandats.com/"}

		if self.brand == "analystq":
			return {"crm": "https://analystq.ptscrm.com/v2", "ca": "http://www.analystq.com"}

		if self.brand == "4ex7":
			return {"crm": "https://4ex7.ptscrm.com/v2", "ca": "https://www.4ex7.com/"}

		if self.brand == "trade99":
			return {"crm": "https://trade99.ptscrm.com/v2", "ca": "http://www.trade99.com"}

		if self.brand == "any1profit":
			return {"crm": "https://any1profit.ptscrm.com/v2", "ca": "https://www.any1profit.com"}

		if self.brand == "bfx":
			return {"crm": "https://bfxinternational.ptscrm.com/v2", "ca": "https://bfxinternational.com/"}

		if self.brand == "brokerz":
			return {"crm": "https://brokerz.ptscrm.com/v2", "ca": "https://brokerz.com/"}

		if self.brand == "wdcmarkets":
			return {"crm": "https://wdcmarkets.ptscrm.com/v2", "ca": "https://wdcmarkets.com/"}

		if self.brand == "brokerz":
			return {"crm": "https://brokerz.ptscrm.com/v2", "ca" : "https://www.brokerz.com/"}



		else:
			return print("brand name was not found, please check 'BrandsList' class ")
