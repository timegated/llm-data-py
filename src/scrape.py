from scrapeghost import SchemaScraper

scrape_legislators = SchemaScraper(
  schema={
      "name": "string",
      "url": "url",
      "district": "string",
      "party": "string",
      "photo_url": "url",
      "offices": [{"name": "string", "address": "string", "phone": "string"}],
  }
)

resp = scrape_legislators("https://www.ilga.gov/house/rep.asp?MemberID=3071")

resp.data
