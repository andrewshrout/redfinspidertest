# redfinspidertest

Scraper that uses the Scrapy framework to acquire data for real estate analysis pipeline. It collects price, estimated monthly payments, features, descriptions, neighborhood, and location data for every listing on redfin.

## How to Use

Notebooks/listing.ipynb contains the selectors to break down each listing.

Notebooks/listings.ipynb contains selectors for selecting all links within a city.

Notebooks/sitemap.ipynb contains a list of all citys and countys on redfin.

## Data Dictionary
```
'locality': name of the city the property is in
'postalCode': 5 digit postal code
'region': state
'street': street address of property (for geocoding)
'agentName': sellers agent representing the property
'company': real estate brokerage who employs the agent
'bath': # of bathrooms
'beds': # of bedrooms
'compensation': % cut the brokerage will take out of the sale
'buildDate': year the property was built
'description': string describing the property, used to ascertain length/quality of sales copy or parse additional features.
'moPayment': monthly estimated payment on mortgage according to redfin
'principalInterest': breakdown of payments
'propertyTax': estimated monthly taxes
'hoaDues': estimated HOA dues
'insurance': estimated homeowners insurance
'status': is the property currently being sold?
'redfinTime': how long has the property been listed?
'propertyType': Is the property an apartment, house, condo, etc?
'style': Is the house traditional, craftsmen, etc?
'community': string name for the neighborhood
'lotSize': sq footage of the property
'mlsNum': # of the property on the multiple listing service
'price': asking sales price of the property
'priceSqFt': sales price / square footage of the property
'propDetails': a dictionary of features the property may contain, like parking, exterior features, nearby schools, etc
```


## TODO:

1. Scale with scrapy
2. Automate cleaner on lambda (break apart the feature dictionary into parseable categories)

## Authors

Andrew Shrout

