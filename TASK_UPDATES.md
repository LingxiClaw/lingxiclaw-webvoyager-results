# Task Collection and Instruction Updates

The exact evaluated collection contains **615 tasks** from **15 websites**, with SHA-256 `e0f99161eeb09f30c94cb687143b67e6684347dc29ba863541f95ba15914f9b9`.

- [Exact evaluated task file](evaluated-615.jsonl)
- [Canonical 643-task reference](original-643.jsonl)
- [Complete structured provenance](dataset-provenance.json)
- [Canonical snapshot](https://github.com/MinorJerry/WebVoyager/tree/5a7896738c10bfb8b9edccce6bb0e0411f8ae569)
- [Fixed omxyz comparison snapshot](https://github.com/omxyz/webvoyager/tree/df42681582be8125c5296473ad8efcd86f926cb6)

There are 28 excluded canonical IDs: the inherited 24-task Alumnium exclusion set and four additional upstream exclusions. No extra task was removed based on Lingxi's outcomes. Among retained tasks, 99 instructions differ from canonical and 71 differ from the fixed omxyz current layer. The latter differences are date replacements or explicit date-format/year normalization in Booking and Google Flights. Counts refer to changed questions, not changed tokens.

The historical editing command and author intent were not recovered. The before/after comparisons below describe the recovered files. Booking--5 requests October 1–4, 2026, already past at execution on October 9; its failure remains in the denominator.

## Excluded task IDs

| Task ID | Upstream group | Recorded basis |
| --- | --- | --- |
| Allrecipes--16 | alumnium-24 | Member of the upstream 24-task Alumnium exclusion list; individual rationale is not supplied in that list. |
| Allrecipes--19 | alumnium-24 | Member of the upstream 24-task Alumnium exclusion list; individual rationale is not supplied in that list. |
| Allrecipes--29 | current-additional-4 | The upstream authors did not verify a current recipe satisfying all fish, olives, rating and review constraints. |
| Allrecipes--3 | alumnium-24 | Member of the upstream 24-task Alumnium exclusion list; individual rationale is not supplied in that list. |
| Allrecipes--30 | alumnium-24 | Member of the upstream 24-task Alumnium exclusion list; individual rationale is not supplied in that list. |
| Amazon--19 | alumnium-24 | Member of the upstream 24-task Alumnium exclusion list; individual rationale is not supplied in that list. |
| Apple--42 | alumnium-24 | Member of the upstream 24-task Alumnium exclusion list; individual rationale is not supplied in that list. |
| Apple--7 | alumnium-24 | Member of the upstream 24-task Alumnium exclusion list; individual rationale is not supplied in that list. |
| Apple--9 | current-additional-4 | The upstream authors identified an outdated pickup date outside the available checkout window. |
| BBC News--18 | alumnium-24 | Member of the upstream 24-task Alumnium exclusion list; individual rationale is not supplied in that list. |
| BBC News--29 | alumnium-24 | Member of the upstream 24-task Alumnium exclusion list; individual rationale is not supplied in that list. |
| BBC News--37 | alumnium-24 | Member of the upstream 24-task Alumnium exclusion list; individual rationale is not supplied in that list. |
| Booking--11 | alumnium-24 | Member of the upstream 24-task Alumnium exclusion list; individual rationale is not supplied in that list. |
| Booking--13 | alumnium-24 | Member of the upstream 24-task Alumnium exclusion list; individual rationale is not supplied in that list. |
| Booking--14 | alumnium-24 | Member of the upstream 24-task Alumnium exclusion list; individual rationale is not supplied in that list. |
| Booking--6 | alumnium-24 | Member of the upstream 24-task Alumnium exclusion list; individual rationale is not supplied in that list. |
| Cambridge Dictionary--19 | current-additional-4 | Upstream translation-provider attribution was blocked by verification challenges. |
| Cambridge Dictionary--41 | alumnium-24 | Member of the upstream 24-task Alumnium exclusion list; individual rationale is not supplied in that list. |
| Coursera--17 | alumnium-24 | Member of the upstream 24-task Alumnium exclusion list; individual rationale is not supplied in that list. |
| Coursera--28 | alumnium-24 | Member of the upstream 24-task Alumnium exclusion list; individual rationale is not supplied in that list. |
| Google Flights--0 | alumnium-24 | Member of the upstream 24-task Alumnium exclusion list; individual rationale is not supplied in that list. |
| Google Flights--20 | alumnium-24 | Member of the upstream 24-task Alumnium exclusion list; individual rationale is not supplied in that list. |
| Google Map--13 | alumnium-24 | Member of the upstream 24-task Alumnium exclusion list; individual rationale is not supplied in that list. |
| Google Search--22 | alumnium-24 | Member of the upstream 24-task Alumnium exclusion list; individual rationale is not supplied in that list. |
| Huggingface--1 | current-additional-4 | The requested inference API path required authentication in the upstream anonymous setup. |
| Huggingface--10 | alumnium-24 | Member of the upstream 24-task Alumnium exclusion list; individual rationale is not supplied in that list. |
| Huggingface--32 | alumnium-24 | Member of the upstream 24-task Alumnium exclusion list; individual rationale is not supplied in that list. |
| Huggingface--6 | alumnium-24 | Member of the upstream 24-task Alumnium exclusion list; individual rationale is not supplied in that list. |

## Differences from the canonical task questions

### Booking--0

**Canonical:**

Find a Mexico hotel with deals for December 25-26.

**Evaluated:**

Find a Mexico hotel with deals for December 25, 2026 to December 26, 2026.

### Google Flights--1

**Canonical:**

Show me the list of one-way flights today (February 17, 2024) from Chicago to Paris.

**Evaluated:**

Show me the list of one-way flights on December 9, 2026 from Chicago to Paris.

### Amazon--1

**Canonical:**

Search for women's golf polos in m size, priced between 50 to 75 dollars, and save the lowest priced among results.

**Evaluated:**

Search for women's golf polos in m size, priced between 50 to 75 dollars, and add the lowest priced among results to cart.

### Booking--1

**Canonical:**

Find the cheapest available hotel room for a three night stay from 1st Jan in Jakarta. The room is for 2 adults, just answer the cheapest hotel room and the price.

**Evaluated:**

Find the cheapest available hotel room for a three night stay from November 23, 2026 in Jakarta. The room is for 2 adults, just answer the cheapest hotel room and the price.

### Google Flights--2

**Canonical:**

Find the lowest fare from all eligible one-way flights for 1 adult from JFK to Heathrow on Jan. 22.

**Evaluated:**

Find the lowest fare from all eligible one-way flights for 1 adult from JFK to Heathrow on December 14, 2026.

### BBC News--2

**Canonical:**

Read the latest article regarding the environmental impacts of deforestation published within the last two days.

**Evaluated:**

Read the latest article regarding the environmental impacts of deforestation published within the last two months.

### Booking--2

**Canonical:**

Find a hotel in Ohio From December 20th to December 23th for 3 adults and 2 rooms.

**Evaluated:**

Find a hotel in Ohio From December 20, 2026 to December 23, 2026 for 3 adults and 2 rooms.

### Google Flights--3

**Canonical:**

Search for the one-way flight available from Calgary to New York on Jan. 1st with the lowest carbon dioxide emissions.

**Evaluated:**

Search for the one-way flight available from Calgary to New York on January 1, 2027 with the lowest carbon dioxide emissions.

### Booking--3

**Canonical:**

Find a hotel with 4 star and above rating in Los Angeles for 3 days from Dec 18th.

**Evaluated:**

Find a hotel with 4 star and above rating in Los Angeles for 3 days from January 9, 2027.

### Google Flights--4

**Canonical:**

Search for one-way flights from New York to London on Dec. 26th and filter the results to show only non-stop flights.

**Evaluated:**

Search for one-way flights from New York to London on December 26, 2026 and filter the results to show only non-stop flights.

### Apple--4

**Canonical:**

How much does it cost to buy a Macbook pro, 16-inch, Apple M3 Max chip with 16-core CPU, 40-core GPU, 64GB unified memory, 1TB SSD.

**Evaluated:**

How much does it cost to buy a Macbook pro, 16-inch, Apple M4 Max chip with 16-core CPU, 40-core GPU, 64GB unified memory, 1TB SSD.

### Booking--4

**Canonical:**

Search for the cheapest Hotel near Kashi Vishwanath Temple that offer breakfast from Dec 25th - Dec 26th.

**Evaluated:**

Search for the cheapest Hotel near Kashi Vishwanath Temple that offer breakfast from December 25, 2026 - December 26, 2026.

### Google Flights--5

**Canonical:**

Find flights from Chicago to London on 20 December and return on 23 December.

**Evaluated:**

Find flights from Chicago to London on December 20, 2026 and return on December 23, 2026.

### Booking--5

**Canonical:**

Search a hotel with free WiFi and air conditioning in Bali from Jan 1 to Jan 4, 2024.

**Evaluated:**

Search a hotel with free WiFi and air conditioning in Bali from October 1, 2026 to October 4, 2026.

### Google Flights--6

**Canonical:**

Search for a flight on December 19 and return on December 26 from Tel Aviv to Venice and Select First Class.

**Evaluated:**

Search for a flight on December 19, 2026 and return on December 26, 2026 from Tel Aviv to Venice and Select First Class.

### Amazon--6

**Canonical:**

Browse black strollers within $100 to $200 on Amazon. Then find one Among these black strollers with over 20,000 reviews and a rating greater than 4 star.

**Evaluated:**

Browse black strollers within $100 to $200 on Amazon. Then find one Among these black strollers with over 2,000 reviews and a rating greater than 4 star.

### Booking--7

**Canonical:**

Find a hotel room on January 3-6 that is closest to National University of Singapore and costs less than $500

**Evaluated:**

Find a hotel room on January 3, 2027 to January 6, 2027 that is closest to National University of Singapore and costs less than $500

### Google Flights--7

**Canonical:**

Find a round trip from Phoenix to Miami (Dec. 25th - Dec. 28th), show the First Class plane tickets for me that do not exceed $1320..

**Evaluated:**

Find a round trip from Phoenix to Miami (December 29, 2026 - January 1, 2027), show the First Class plane tickets for me that do not exceed $2000.

### Booking--8

**Canonical:**

Get the hotel with highest review score and free cancelation in Chennai for 20/12/2023 - 21/12/2023.

**Evaluated:**

Get the hotel with highest review score and free cancelation in Chennai for December 20, 2026 - December 21, 2026.

### Google Flights--8

**Canonical:**

Search a one-way filght from Dublin To Athens Greece for 1 Adult that leaves on December 30 and analyse the price graph for the next 2 months.

**Evaluated:**

Search a one-way filght from Dublin To Athens Greece for 1 Adult that leaves on December 30, 2026 and analyse the price graph for the next 2 months.

### Booking--9

**Canonical:**

Find hotels for 2 adults in London with a price less than 250 dollars for four days starting from December 25. You must browse the page and offer at least 3 options.

**Evaluated:**

Find hotels for 2 adults in London with a price less than 250 dollars for four days starting from December 25, 2026. You must browse the page and offer at least 3 options.

### Google Flights--9

**Canonical:**

Find a one way economy flight from Pune to New York in Jan. 15th and show me how long it will take for flight transfer.

**Evaluated:**

Find a one way economy flight from Pune to New York in January 15, 2027 and show me how long it will take for flight transfer.

### Booking--10

**Canonical:**

Find a well-reviewed hotel in Paris with available bookings suitable for a couple (2 adults) on Valentine's Day week, February 14-21, 2024, that offers free cancellation options.

**Evaluated:**

Find a well-reviewed hotel in Paris with available bookings suitable for a couple (2 adults) on Valentine's Day week, February 14, 2027 to February 21, 2027, that offers free cancellation options.

### Google Flights--10

**Canonical:**

Locate the cheapest round-trip flights from New York to Tokyo leaving on January 25, 2024, and returning on February 15, 2024.

**Evaluated:**

Locate the cheapest round-trip flights from New York to Tokyo leaving on October 17, 2026, and returning on November 6, 2026.

### Booking--12

**Canonical:**

Find a hotel in Paris with a customer review score of 8 or higher, free Wi-Fi, and available for a 5-night stay starting on January 5th, 2024.

**Evaluated:**

Find a hotel in Paris with a customer review score of 8 or higher, free Wi-Fi, and available for a 5-night stay starting on January 5, 2027.

### Google Flights--11

**Canonical:**

Compare the prices for round-trip flights from New York to Tokyo for a departure on February 10, 2024, and a return on February 24, 2024, and select the option with the least number of stops.

**Evaluated:**

Compare the prices for round-trip flights from New York to Tokyo for a departure on January 1, 2027, and a return on January 15, 2027, and select the option with the least number of stops.

### Booking--15

**Canonical:**

Find the highest-rated luxury hotel in Rome available for booking from January 10, 2024, to January 20, 2024, for 2 adults. Include the cost, amenities offered, and customer rating.

**Evaluated:**

Find the highest-rated luxury hotel in Rome available for booking from January 10, 2027, to January 20, 2027, for 2 adults. Include the cost, amenities offered, and customer rating.

### Google Flights--12

**Canonical:**

Find the best-priced round-trip flight from New York to London leaving on December 25, 2023, and returning on January 5, 2024, with one stop or fewer.

**Evaluated:**

Find the best-priced round-trip flight from New York to London leaving on December 17, 2026, and returning on December 27, 2026, with one stop or fewer.

### Apple--14

**Canonical:**

Identify the upgrade options available for the cheapest base model of the MacBook Pro 14-inch with M3 chip, and calculate the total price difference from the base model to the maximum upgrade (no Pre-Installed Software) offered by Apple.

**Evaluated:**

Identify the upgrade options available for the cheapest base model of the MacBook Pro 14-inch with M5 chip, and calculate the total price difference from the base model to the maximum upgrade (no Pre-Installed Software) offered by Apple.

### Booking--16

**Canonical:**

Look for a hotel in Paris with a user rating of 9 or higher and available for a 5-night stay starting January 15, 2024. The hotel should also offer free Wi-Fi and breakfast included in the price. Provide the name, location, and price per night.

**Evaluated:**

Look for a hotel in Paris with a user rating of 9 or higher and available for a 5-night stay starting January 15, 2027. The hotel should also offer free Wi-Fi and breakfast included in the price. Provide the name, location, and price per night.

### Google Flights--13

**Canonical:**

Find the cheapest round-trip flight option from New York City to Tokyo for a departure on January 10, 2024, and a return on January 24, 2024.

**Evaluated:**

Find the cheapest round-trip flight option from New York City to Tokyo for a departure on January 1, 2027, and a return on January 15, 2027.

### Booking--17

**Canonical:**

Find a hotel in Paris with a fitness center and a rating of 8 or higher available for a 5-night stay starting from February 14, 2024, and sort the results by best reviewed.

**Evaluated:**

Find a hotel in Paris with a fitness center and a rating of 8 or higher available for a 5-night stay starting from February 14, 2027, and sort the results by best reviewed.

### GitHub--13

**Canonical:**

Identify the latest top-trending open-source project in the category of 'Machine Learning' on GitHub, and check the number of stars it has received.

**Evaluated:**

Identify the latest top-trending open-source project in the topic of 'Machine Learning' on GitHub, and check the number of stars it has received.

### Google Flights--14

**Canonical:**

Compare flight options and find the lowest round trip fare from New York to London departing on January 10, 2024, and returning on January 17, 2024.

**Evaluated:**

Compare flight options and find the lowest round trip fare from New York to London departing on January 1, 2027, and returning on January 8, 2027.

### Booking--18

**Canonical:**

Search a hotel in London with a user rating of 8 or higher for a stay between February 14th, 2024, and February 21st, 2024, suitable for a couple. Provide the name and a short description of the hotel.

**Evaluated:**

Search a hotel in London with a user rating of 8 or higher for a stay between February 14, 2027, and February 21, 2027, suitable for a couple. Provide the name and a short description of the hotel.

### Google Flights--15

**Canonical:**

Compare the prices and total duration of non-stop flights from New York to Tokyo Narita Airport departing on February 12th, 2024, and returning on February 26th, 2024.

**Evaluated:**

Compare the prices and total duration of non-stop flights from New York to Tokyo Narita Airport departing on January 3, 2027, and returning on January 17, 2027.

### Booking--19

**Canonical:**

Look for a hotel with customer ratings above an 8.0 in Paris, France for a weekend stay from March 18, 2024, to March 20, 2024, and list top three suggestions based on user reviews.

**Evaluated:**

Look for a hotel with customer ratings above an 8.0 in Paris, France for a weekend stay from February 13, 2027, to February 15, 2027, and list top three suggestions based on user reviews.

### ESPN--15

**Canonical:**

Check the scores of the NBA games played on December 25, 2023.

**Evaluated:**

Check the scores of the NBA games played on February 25, 2026.

### Google Flights--16

**Canonical:**

Find the cheapest one-way flight from New York to Tokyo departing on January 15, 2024, and provide the airline and total flight duration.

**Evaluated:**

Find the cheapest one-way flight from New York to Tokyo departing on January 15, 2027, and provide the airline and total flight duration.

### Booking--20

**Canonical:**

Locate a hotel in Rome with a good rating (7 or above) that offers free cancellation and breakfast included, for a three-night stay from February 28 to March 2, 2024, for two adults.

**Evaluated:**

Locate a hotel in Rome with a good rating (7 or above) that offers free cancellation and breakfast included, for a stay from October 28, 2026 to November 2, 2026, for two adults.

### ESPN--16

**Canonical:**

Check the schedule for the NBA game on December 25, 2023, and provide the teams that are playing and their current standings in their respective conferences.

**Evaluated:**

Check the schedule for the NBA game on February 25, 2026, and provide the teams that are playing and their current standings in their respective conferences.

### Google Flights--17

**Canonical:**

Find the cheapest round-trip flight from New York to Paris leaving on December 27, 2023, and returning on January 10, 2024.

**Evaluated:**

Find the cheapest round-trip flight from New York to Paris leaving on December 19, 2026, and returning on January 1, 2027.

### Booking--21

**Canonical:**

Find a hotel in Sydney with a rating of 8 or higher, providing free Wi-Fi and parking, available for a four-night stay starting on March 10, 2024.

**Evaluated:**

Find a hotel in Sydney with a rating of 8 or higher, providing free Wi-Fi and parking, available for a four-night stay starting on January 1, 2027.

### ESPN--17

**Canonical:**

Check out the NBA Basketball Power Index 2023-24 to see which teams are in first place and which are in last place.

**Evaluated:**

Check out the NBA Basketball Power Index 2025-26 to see which teams are in first place and which are in last place.

### Google Flights--18

**Canonical:**

Compare flight options from New York to Tokyo for a round trip leaving on January 25, 2024, and returning on February 15, 2024, for one adult. Prioritize the comparisons by the shortest travel time.

**Evaluated:**

Compare flight options from New York to Tokyo for a round trip leaving on December 17, 2026, and returning on January 6, 2027, for one adult. Prioritize the comparisons by the shortest travel time.

### Huggingface--20

**Canonical:**

Locate a pre-trained natural language processing model on Hugging Face that specializes in named entity recognition (NER), confirm that the model was last updated in 2022 and has 1M+ downloads.

**Evaluated:**

Locate a pre-trained natural language processing model on Hugging Face that specializes in named entity recognition (NER), confirm that the model was last updated in 2024 and has 1M+ downloads.

### Apple--20

**Canonical:**

Check the price for an Apple iPhone 14 Plus with 256GB storage in Purple color.

**Evaluated:**

Check the price for an Apple iPhone 17 with 256GB storage in Purple color.

### Booking--22

**Canonical:**

Search for a hotel in Amsterdam with a customer review score of 9 or higher, offering bicycle rentals, for a week-long stay from March 15 to March 22, 2024, for two adults.

**Evaluated:**

Search for a hotel in Amsterdam with a customer review score of 9 or higher, offering bicycle rentals, for a week-long stay from December 7, 2026 to December 14, 2026, for two adults.

### Google Flights--19

**Canonical:**

Find the cheapest one-way flight from London to Paris, departing on January 25, 2024. Include the airline, total travel time, and layovers for the chosen flight.

**Evaluated:**

Find the cheapest one-way flight from London to Paris, departing on January 16, 2027. Include the airline, total travel time, and layovers for the chosen flight.

### Amazon--20

**Canonical:**

Search for a wireless ergonomic keyboard with backlighting and a rating of at least 4 stars. The price should be between $40 to $60. Save the product with the 500+ customer reviews.

**Evaluated:**

Search for a wireless ergonomic keyboard with backlighting and a rating of at least 4 stars. The price should be between $40 to $60. Add the product with the 500+ customer reviews to cart.

### Booking--23

**Canonical:**

Identify a hotel in Tokyo with a spa and wellness center, rated 9 or above, with availability for a five-night stay starting on February 20, 2024. Check if free cancellation is offered.

**Evaluated:**

Identify a hotel in Tokyo with a spa and wellness center, rated 9 or above, with availability for a five-night stay starting on December 12, 2026. Check if free cancellation is offered.

### Google Flights--21

**Canonical:**

Locate the lowest-priced one-way flight from Tokyo to Sydney for an adult, departing on February 25, 2024, and include the flight duration and number of layovers.

**Evaluated:**

Locate the lowest-priced one-way flight from Tokyo to Sydney for an adult, departing o6 January 16, 2027, and include the flight duration and number of layovers.

### Apple--22

**Canonical:**

Find out the trade-in value for an iPhone 13 Pro Max in good condition on the Apple website.

**Evaluated:**

Find out the trade-in value for an iPhone 15 Pro Max in good condition on the Apple website.

### Booking--24

**Canonical:**

Find a hotel in Barcelona for a stay from February 25-28, 2024. Please sort the results by distance from the beach and make sure they offer free Wi-Fi and breakfast.

**Evaluated:**

Find a hotel in Barcelona for a stay from February 25, 2027 to February 28, 2027. Please sort the results by distance from the beach and make sure they offer free Wi-Fi and breakfast.

### Google Flights--22

**Canonical:**

Find a round-trip flight from Rio de Janeiro to Los Angeles, leaving on March 15, 2024, and returning on March 22, 2024, and select the option with the least carbon dioxide emissions.

**Evaluated:**

Find a round-trip flight from Rio de Janeiro to Los Angeles, leaving on December 7, 2026, and returning on December 14, 2026, and select the option with the least carbon dioxide emissions.

### Booking--25

**Canonical:**

Search for a hotel in Lisbon with airport shuttle, rated 8.5 or above, available for a six-night stay from March 1 to March 7, 2024, for two adults, breakfast included.

**Evaluated:**

Search for a hotel in Lisbon with airport shuttle, rated 8.5 or above, available for a six-night stay from January 23, 2027 to January 29, 2027, for two adults, breakfast included.

### Google Flights--23

**Canonical:**

Search for a one-way flight from Mumbai to Vancouver on February 28, 2024, filtering the results to show only 1-stop flights.

**Evaluated:**

Search for a one-way flight from Mumbai to Vancouver on January 19, 2027, filtering the results to show only 1-stop flights.

### Booking--26

**Canonical:**

Check Booking.com for a 3-star hotel or higher in Paris with a guest rating above 8.0 and available parking for dates February 20-23, 2024.

**Evaluated:**

Check Booking.com for a 3-star hotel or higher in Paris with a guest rating above 8.0 and available parking for dates January 11, 2027 to January 14, 2027.

### Google Flights--24

**Canonical:**

Compare prices for economy class round-trip flights from Dubai to Rome, departing on March 1, 2024, and returning on March 8, 2024, and select the option with the fewest stops.

**Evaluated:**

Compare prices for economy class round-trip flights from Dubai to Rome, departing on December 23, 2026, and returning on December 30, 2026, and select the option with the fewest stops.

### ArXiv--23

**Canonical:**

Determine how many articles with the keyword 'autonomous vehicles' were published in the 'Electrical Engineering and Systems Science' section of ArXiv yesterday.

**Evaluated:**

Determine how many articles with the keyword 'autonomous vehicles' were published in the 'Electrical Engineering and Systems Science' section of ArXiv last week.

### Booking--27

**Canonical:**

Locate a hotel in Melbourne offering free parking and free WiFi, for a stay from February 28 to March 4, 2024.

**Evaluated:**

Locate a hotel in Melbourne offering free parking and free WiFi, for a stay from December 20, 2026 to December 26, 2026.

### Google Flights--25

**Canonical:**

Find a one-way business class flight from Buenos Aires to Amsterdam on March 10, 2024, and provide the details of the flight with the shortest duration.

**Evaluated:**

Find a one-way business class flight from Buenos Aires to Amsterdam on January 1, 2027, and provide the details of the flight with the shortest duration.

### Booking--28

**Canonical:**

Find a hotel in Dubai with a swimming pool, for a week-long stay from February 22 to February 29, 2024.

**Evaluated:**

Find a hotel in Dubai with a swimming pool, for a week-long stay from December 14, 2026 to December 21, 2026.

### Google Flights--26

**Canonical:**

Search for the cheapest round-trip flights from Bangkok to Madrid, leaving on February 26, 2024, and returning on February 28, 2024, and provide options under $1000.

**Evaluated:**

Search for the cheapest round-trip flights from Bangkok to Madrid, leaving on January 17, 2027, and returning on January 19, 2027, and provide options under $1000.

### Booking--29

**Canonical:**

Search for a hotel in Toronto with a fitness center and a rating of 8+, available for a two-night stay from March 5 to March 7, 2024.

**Evaluated:**

Search for a hotel in Toronto with a fitness center and a rating of 8+, available for a two-night stay from December 27, 2026 to December 29, 2026.

### Google Flights--27

**Canonical:**

Locate a one-way flight from Johannesburg to Toronto on March 30, 2024, for one adult, and analyze the price trends for the following month.

**Evaluated:**

Locate a one-way flight from Johannesburg to Toronto on January 21, 2027, for one adult, and analyze the price trends for the following month.

### ArXiv--26

**Canonical:**

Search for papers related to 'climate change modeling' on ArXiv and find out how many have been published in the Earth and Planetary Astrophysics (astro-ph.EP) category in the last week.

**Evaluated:**

Search for papers related to 'climate change modeling' on ArXiv and find out how many have been published in the Earth and Planetary Astrophysics (astro-ph.EP) category in the last month.

### Booking--30

**Canonical:**

Search for hotels in London from March 20 to March 23, 2024, on Booking. How many hotels are left after applying the Breakfast included and Fitness center filters?

**Evaluated:**

Search for hotels in London from January 11, 2027 to January 14, 2027, on Booking. How many hotels are left after applying the Breakfast included and Fitness center filters?

### Google Flights--28

**Canonical:**

Find the best-priced round-trip flight from Seattle to Paris, departing on February 27, 2024, and returning on March 1, 2024, with a maximum of one stop.

**Evaluated:**

Find the best-priced round-trip flight from Seattle to Paris, departing on January 18, 2027, and returning on January 23, 2027, with a maximum of one stop.

### Booking--31

**Canonical:**

Search for hotels in Rio de Janeiro from March 1-7, 2024, check the Brands filter to see which brand has the most hotels and which brand has the fewest.

**Evaluated:**

Search for hotels in Rio de Janeiro from December 23, 2026 to December 29, 2026, check the Brands filter to see which brand has the most hotels and which brand has the fewest.

### Google Flights--29

**Canonical:**

Compare the prices and total travel time of non-stop flights from Mexico City to Frankfurt, departing on March 5, 2024, and returning on March 15, 2024.

**Evaluated:**

Compare the prices and total travel time of non-stop flights from Mexico City to Frankfurt, departing on December 27, 2026, and returning on January 6, 2027.

### Booking--32

**Canonical:**

Look for hotels in Sydney from February 24 to February 27, 2024, on Booking. Once the Swimming Pool and Airport Shuttle filters are applied, what is the total number of hotels available?

**Evaluated:**

Look for hotels in Sydney from February 24, 2027 to February 27, 2027, on Booking. Once the Swimming Pool and Airport Shuttle filters are applied, what is the total number of hotels available?

### Google Flights--30

**Canonical:**

Find the most affordable one-way flight from Cape Town to Singapore, departing on March 20, 2024, and include the airline and total number of layovers.

**Evaluated:**

Find the most affordable one-way flight from Cape Town to Singapore, departing on January 11, 2027, and include the airline and total number of layovers.

### Amazon--30

**Canonical:**

Locate the highest-rated fiction book released in 2024 on Amazon, with a minimum of 50 customer reviews.

**Evaluated:**

Locate the highest-rated fiction book released in 2026 on Amazon, with a minimum of 50 customer reviews.

### Google Flights--31

**Canonical:**

Find a one-way economy flight from Auckland to Honolulu on March 25, 2024, browse the full page and display a flight option with the most stops.

**Evaluated:**

Find a one-way economy flight from Auckland to Honolulu on January 16, 2027, browse the full page and display a flight option with the most stops.

### Apple--32

**Canonical:**

Investigate the trade-in value for an iPhone 11 Pro Max on Apple's website.

**Evaluated:**

Investigate the trade-in value for an iPhone 13 Pro Max on Apple's website.

### Booking--34

**Canonical:**

Search for a hotel in Berlin available for a three-night stay from March 15 to March 18, 2024, for one adult. Tell me the price in USD and CNY for the three-night stay.

**Evaluated:**

Search for a hotel in Berlin available for a three-night stay from January 6, 2027 to January 9, 2027, for one adult. Tell me the price in USD and CNY for the three-night stay.

### ESPN--30

**Canonical:**

Check out the NHL Standings 2023-24 on ESPN to see which teams are at the top and which are at the bottom in Eastern and Western Conference. What about the situation in Division.

**Evaluated:**

Check out the NHL Standings 2025-26 on ESPN to see which teams are at the top and which are at the bottom in Eastern and Western Conference. What about the situation in Division.

### Google Flights--32

**Canonical:**

Search for round-trip flights from Stockholm to Toronto, departing on March 3, 2024, and returning on March 10, 2024, and sort the results to find the shortest total travel time.

**Evaluated:**

Search for round-trip flights from Stockholm to Toronto, departing on December 25, 2026, and returning on January 1, 2027, and sort the results to find the shortest total travel time.

### ESPN--31

**Canonical:**

Who has the heaviest weight among infielders in the New York Yankees Roster 2023-24?

**Evaluated:**

Who has the heaviest weight among infielders in the New York Yankees Roster 2026?

### Google Flights--33

**Canonical:**

Find a one-way flight from Shanghai to Vancouver on February 27, 2024, and compare the options based on carbon dioxide emissions.

**Evaluated:**

Find a one-way flight from Shanghai to Vancouver on January 18, 2027, and compare the options based on carbon dioxide emissions.

### Booking--36

**Canonical:**

Search for a budget hotel in Rome under $100 per night for one adult from March 20 to March 23, 2024. Sort the results by price, identify if any of top three results offer breakfast.

**Evaluated:**

Search for a budget hotel in Rome under $100 per night for one adult from January 11, 2027 to January 14, 2027. Sort the results by price, identify if any of top three results offer breakfast.

### Google Flights--34

**Canonical:**

Compare business class flight options from Lisbon to Singapore for a one-way trip on March 15, 2024, select one of the flights and see which websites offer its booking options. Which one is the cheapest.

**Evaluated:**

Compare business class flight options from Lisbon to Singapore for a one-way trip on January 6, 2027, select one of the flights and see which websites offer its booking options. Which one is the cheapest.

### Booking--37

**Canonical:**

Search for a resort (not hotel) in Bali, detailing the available dates between March 20, 2024, and March 25, 2024, and checking any provided tour or cultural experiences.

**Evaluated:**

Search for a resort (not hotel) in Bali, detailing the available dates between January 11, 2027, and January 16, 2027, and checking any provided tour or cultural experiences.

### ESPN--33

**Canonical:**

Locate the latest ESPN articles discussing potential MVP candidates in the NFL for 2023 season.

**Evaluated:**

Locate the latest ESPN articles discussing potential MVP candidates in the NFL for 2025 season.

### Google Flights--35

**Canonical:**

Find the lowest-priced one-way flight from Cairo to Montreal on February 21, 2024, including the total travel time and number of stops.

**Evaluated:**

Find the lowest-priced one-way flight from Cairo to Montreal on January 12, 2027, including the total travel time and number of stops.

### Wolfram Alpha--33

**Canonical:**

Identify the electrical energy output of a hydroelectric power plant named Itaipu Dam in 2023 using Wolfram Alpha.

**Evaluated:**

Identify the electrical energy output of a hydroelectric power plant named Itaipu Dam in 2024 using Wolfram Alpha.

### Booking--38

**Canonical:**

Look up Vienna hotel options with availability for a 4-night stay from February 28 to March 4, 2024, with amenities that include a Parking, breakfast included, and a rating of 8+ on Booking.com.

**Evaluated:**

Look up Vienna hotel options with availability for a 4-night stay from December 20, 2026 to December 24, 2026, with amenities that include a Parking, breakfast included, and a rating of 8+ on Booking.com.

### Coursera--36

**Canonical:**

Browse Coursera, which universities offer Master of Advanced Study in Engineering degrees? Tell me what is the latest application deadline for this degree?

**Evaluated:**

Browse Coursera, which universities offer Master of Computer Science degrees? Tell me what is the latest application deadline for this degree?

### Google Flights--36

**Canonical:**

Search for round-trip flights from Helsinki to New Delhi, departing on March 28, 2024, and returning on April 4, 2024, and filter the results to show only flights under $1000.

**Evaluated:**

Search for round-trip flights from Helsinki to New Delhi, departing on January 19, 2027, and returning on January 26, 2027, and filter the results to show only flights under $1000.

### Booking--39

**Canonical:**

Find a pet-friendly hotel with parking available in downtown Toronto for the stay of February 24-26, 2024.

**Evaluated:**

Find a pet-friendly hotel with parking available in downtown Toronto for the stay of January 15, 2027 to January 17, 2027.

### Google Flights--37

**Canonical:**

Locate a round-trip flight from Buenos Aires to Beijing, leaving on February 28, 2024, and returning on March 3, 2024, check out one of the options and tell me if the airline for my return flight is the same as my departure flight.

**Evaluated:**

Locate a round-trip flight from Buenos Aires to Beijing, leaving on December 20, 2026, and returning on December 25, 2026, check out one of the options and tell me if the airline for my return flight is the same as my departure flight.

### Booking--40

**Canonical:**

I need to choose a hotel in Shenzhen, please select date (6 March to 8 March 2024) and click the search button. How much it costs when convert the price to Chinese Yuan on the page.

**Evaluated:**

I need to choose a hotel in Shenzhen, please select date (December 28, 2026 to December 30, 2026) and click the search button. How much it costs when convert the price to Chinese Yuan on the page.

### Google Flights--38

**Canonical:**

Compare the prices and flight durations for economy class flights from Oslo to Dubai, departing on March 8, 2024, and show the options with no more than two layovers.

**Evaluated:**

Compare the prices and flight durations for economy class flights from Oslo to Dubai, departing on December 30, 2026, and show the options with no more than two layovers.

### Google Flights--39

**Canonical:**

Find a one-way flight from Prague to a city in Japan on March 20, 2024, which city in Japan is cheaper to go to, Tokyo or a certain city in Hokkaido?

**Evaluated:**

Find a one-way flight from Prague to a city in Japan on January 11, 2027, which city in Japan is cheaper to go to, Tokyo or a certain city in Hokkaido?

### Booking--42

**Canonical:**

Search for a hotel in Hokkaido for the period March 1 to March 7, 2024, with a rating of 9+, check out its user reviews, which categories are greater than 9 and which are less than 9?

**Evaluated:**

Search for a hotel in Hokkaido for the period December 23, 2026 to December 29, 2026, with a rating of 9+, check out its user reviews, which categories are greater than 9 and which are less than 9?

### Google Search--39

**Canonical:**

Identify the top-10 trending travel destination for 2024 through a blog, how many of them are in Asian.

**Evaluated:**

Identify the top-10 trending travel destination for 2026 through a blog, how many of them are in Asian.

### Apple--41

**Canonical:**

How much does it cost to buy an ipad mini with 64GB storage and Wi-Fi + Cellular connectivity? (no engraving, no apple pencil, no smart folio, no apple trade-in).

**Evaluated:**

How much does it cost to buy an ipad mini with 128GB storage and Wi-Fi + Cellular connectivity? (no engraving, no apple pencil, no smart folio, no apple trade-in).

### Google Flights--41

**Canonical:**

Choose one way business class ticket from Hong Kong to Glacier National Park on 8 March 2024, offering a 1 stop ticket.

**Evaluated:**

Choose one way business class ticket from Hong Kong to Glacier National Park on December 28, 2026, offering a 1 stop ticket.

## Additional differences from the fixed omxyz current layer

### Booking--0

**Fixed omxyz current layer:**

Find a Mexico hotel with deals for December 25-26, 2026.

**Evaluated:**

Find a Mexico hotel with deals for December 25, 2026 to December 26, 2026.

### Google Flights--1

**Fixed omxyz current layer:**

Show me the list of one-way flights on June 17, 2026 from Chicago to Paris.

**Evaluated:**

Show me the list of one-way flights on December 9, 2026 from Chicago to Paris.

### Booking--1

**Fixed omxyz current layer:**

Find the cheapest available hotel room for a three night stay from 1st Jun in Jakarta. The room is for 2 adults, just answer the cheapest hotel room and the price.

**Evaluated:**

Find the cheapest available hotel room for a three night stay from November 23, 2026 in Jakarta. The room is for 2 adults, just answer the cheapest hotel room and the price.

### Google Flights--2

**Fixed omxyz current layer:**

Find the lowest fare from all eligible one-way flights for 1 adult from JFK to Heathrow on Jun. 22.

**Evaluated:**

Find the lowest fare from all eligible one-way flights for 1 adult from JFK to Heathrow on December 14, 2026.

### Booking--2

**Fixed omxyz current layer:**

Find a hotel in Ohio From December 20th to December 23th, 2026 for 3 adults and 2 rooms.

**Evaluated:**

Find a hotel in Ohio From December 20, 2026 to December 23, 2026 for 3 adults and 2 rooms.

### Google Flights--3

**Fixed omxyz current layer:**

Search for the one-way flight available from Calgary to New York on Jan. 1st with the lowest carbon dioxide emissions.

**Evaluated:**

Search for the one-way flight available from Calgary to New York on January 1, 2027 with the lowest carbon dioxide emissions.

### Booking--3

**Fixed omxyz current layer:**

Find a hotel with 4 star and above rating in Los Angeles for 3 days from Jul 18th.

**Evaluated:**

Find a hotel with 4 star and above rating in Los Angeles for 3 days from January 9, 2027.

### Google Flights--4

**Fixed omxyz current layer:**

Search for one-way flights from New York to London on Dec. 26th and filter the results to show only non-stop flights.

**Evaluated:**

Search for one-way flights from New York to London on December 26, 2026 and filter the results to show only non-stop flights.

### Booking--4

**Fixed omxyz current layer:**

Search for the cheapest Hotel near Kashi Vishwanath Temple that offer breakfast from Dec 25th - Dec 26th, 2026.

**Evaluated:**

Search for the cheapest Hotel near Kashi Vishwanath Temple that offer breakfast from December 25, 2026 - December 26, 2026.

### Google Flights--5

**Fixed omxyz current layer:**

Find flights from Chicago to London on 20 December and return on 23 December.

**Evaluated:**

Find flights from Chicago to London on December 20, 2026 and return on December 23, 2026.

### Booking--5

**Fixed omxyz current layer:**

Search a hotel with free WiFi and air conditioning in Bali from October 1 to October 4, 2026.

**Evaluated:**

Search a hotel with free WiFi and air conditioning in Bali from October 1, 2026 to October 4, 2026.

### Google Flights--6

**Fixed omxyz current layer:**

Search for a flight on December 19 and return on December 26 from Tel Aviv to Venice and Select First Class.

**Evaluated:**

Search for a flight on December 19, 2026 and return on December 26, 2026 from Tel Aviv to Venice and Select First Class.

### Booking--7

**Fixed omxyz current layer:**

Find a hotel room on January 3-6 that is closest to National University of Singapore and costs less than $500

**Evaluated:**

Find a hotel room on January 3, 2027 to January 6, 2027 that is closest to National University of Singapore and costs less than $500

### Google Flights--7

**Fixed omxyz current layer:**

Find a round trip from Phoenix to Miami (Jul. 7th - Jul. 10th), show the First Class plane tickets for me that do not exceed $2000.

**Evaluated:**

Find a round trip from Phoenix to Miami (December 29, 2026 - January 1, 2027), show the First Class plane tickets for me that do not exceed $2000.

### Booking--8

**Fixed omxyz current layer:**

Get the hotel with highest review score and free cancelation in Chennai for 20/12/2026 - 21/12/2026.

**Evaluated:**

Get the hotel with highest review score and free cancelation in Chennai for December 20, 2026 - December 21, 2026.

### Google Flights--8

**Fixed omxyz current layer:**

Search a one-way filght from Dublin To Athens Greece for 1 Adult that leaves on December 30 and analyse the price graph for the next 2 months.

**Evaluated:**

Search a one-way filght from Dublin To Athens Greece for 1 Adult that leaves on December 30, 2026 and analyse the price graph for the next 2 months.

### Booking--9

**Fixed omxyz current layer:**

Find hotels for 2 adults in London with a price less than 250 dollars for four days starting from December 25. You must browse the page and offer at least 3 options.

**Evaluated:**

Find hotels for 2 adults in London with a price less than 250 dollars for four days starting from December 25, 2026. You must browse the page and offer at least 3 options.

### Google Flights--9

**Fixed omxyz current layer:**

Find a one way economy flight from Pune to New York in Jan. 15th and show me how long it will take for flight transfer.

**Evaluated:**

Find a one way economy flight from Pune to New York in January 15, 2027 and show me how long it will take for flight transfer.

### Booking--10

**Fixed omxyz current layer:**

Find a well-reviewed hotel in Paris with available bookings suitable for a couple (2 adults) on Valentine's Day week, February 14-21, 2027, that offers free cancellation options.

**Evaluated:**

Find a well-reviewed hotel in Paris with available bookings suitable for a couple (2 adults) on Valentine's Day week, February 14, 2027 to February 21, 2027, that offers free cancellation options.

### Google Flights--10

**Fixed omxyz current layer:**

Locate the cheapest round-trip flights from New York to Tokyo leaving on April 25, 2026, and returning on May 15, 2026.

**Evaluated:**

Locate the cheapest round-trip flights from New York to Tokyo leaving on October 17, 2026, and returning on November 6, 2026.

### Booking--12

**Fixed omxyz current layer:**

Find a hotel in Paris with a customer review score of 8 or higher, free Wi-Fi, and available for a 5-night stay starting on January 5th, 2027.

**Evaluated:**

Find a hotel in Paris with a customer review score of 8 or higher, free Wi-Fi, and available for a 5-night stay starting on January 5, 2027.

### Google Flights--11

**Fixed omxyz current layer:**

Compare the prices for round-trip flights from New York to Tokyo for a departure on July 10, 2026, and a return on July 24, 2026, and select the option with the least number of stops.

**Evaluated:**

Compare the prices for round-trip flights from New York to Tokyo for a departure on January 1, 2027, and a return on January 15, 2027, and select the option with the least number of stops.

### Google Flights--12

**Fixed omxyz current layer:**

Find the best-priced round-trip flight from New York to London leaving on June 25, 2026, and returning on July 5, 2026, with one stop or fewer.

**Evaluated:**

Find the best-priced round-trip flight from New York to London leaving on December 17, 2026, and returning on December 27, 2026, with one stop or fewer.

### Google Flights--13

**Fixed omxyz current layer:**

Find the cheapest round-trip flight option from New York City to Tokyo for a departure on July 10, 2026, and a return on July 24, 2026.

**Evaluated:**

Find the cheapest round-trip flight option from New York City to Tokyo for a departure on January 1, 2027, and a return on January 15, 2027.

### Google Flights--14

**Fixed omxyz current layer:**

Compare flight options and find the lowest round trip fare from New York to London departing on July 10, 2026, and returning on July 17, 2026.

**Evaluated:**

Compare flight options and find the lowest round trip fare from New York to London departing on January 1, 2027, and returning on January 8, 2027.

### Booking--18

**Fixed omxyz current layer:**

Search a hotel in London with a user rating of 8 or higher for a stay between February 14th, 2027, and February 21st, 2027, suitable for a couple. Provide the name and a short description of the hotel.

**Evaluated:**

Search a hotel in London with a user rating of 8 or higher for a stay between February 14, 2027, and February 21, 2027, suitable for a couple. Provide the name and a short description of the hotel.

### Google Flights--15

**Fixed omxyz current layer:**

Compare the prices and total duration of non-stop flights from New York to Tokyo Narita Airport departing on July 12th, 2026, and returning on July 26th, 2026.

**Evaluated:**

Compare the prices and total duration of non-stop flights from New York to Tokyo Narita Airport departing on January 3, 2027, and returning on January 17, 2027.

### Booking--19

**Fixed omxyz current layer:**

Look for a hotel with customer ratings above an 8.0 in Paris, France for a weekend stay from August 18, 2026, to August 20, 2026, and list top three suggestions based on user reviews.

**Evaluated:**

Look for a hotel with customer ratings above an 8.0 in Paris, France for a weekend stay from February 13, 2027, to February 15, 2027, and list top three suggestions based on user reviews.

### Booking--20

**Fixed omxyz current layer:**

Locate a hotel in Rome with a good rating (7 or above) that offers free cancellation and breakfast included, for a stay from October 28 to November 2, 2026, for two adults.

**Evaluated:**

Locate a hotel in Rome with a good rating (7 or above) that offers free cancellation and breakfast included, for a stay from October 28, 2026 to November 2, 2026, for two adults.

### Google Flights--17

**Fixed omxyz current layer:**

Find the cheapest round-trip flight from New York to Paris leaving on June 27, 2026, and returning on July 10, 2026.

**Evaluated:**

Find the cheapest round-trip flight from New York to Paris leaving on December 19, 2026, and returning on January 1, 2027.

### Booking--21

**Fixed omxyz current layer:**

Find a hotel in Sydney with a rating of 8 or higher, providing free Wi-Fi and parking, available for a four-night stay starting on July 10, 2026.

**Evaluated:**

Find a hotel in Sydney with a rating of 8 or higher, providing free Wi-Fi and parking, available for a four-night stay starting on January 1, 2027.

### Google Flights--18

**Fixed omxyz current layer:**

Compare flight options from New York to Tokyo for a round trip leaving on June 25, 2026, and returning on July 15, 2026, for one adult. Prioritize the comparisons by the shortest travel time.

**Evaluated:**

Compare flight options from New York to Tokyo for a round trip leaving on December 17, 2026, and returning on January 6, 2027, for one adult. Prioritize the comparisons by the shortest travel time.

### Booking--22

**Fixed omxyz current layer:**

Search for a hotel in Amsterdam with a customer review score of 9 or higher, offering bicycle rentals, for a week-long stay from June 15 to June 22, 2026, for two adults.

**Evaluated:**

Search for a hotel in Amsterdam with a customer review score of 9 or higher, offering bicycle rentals, for a week-long stay from December 7, 2026 to December 14, 2026, for two adults.

### Google Flights--19

**Fixed omxyz current layer:**

Find the cheapest one-way flight from London to Paris, departing on July 25, 2026. Include the airline, total travel time, and layovers for the chosen flight.

**Evaluated:**

Find the cheapest one-way flight from London to Paris, departing on January 16, 2027. Include the airline, total travel time, and layovers for the chosen flight.

### Booking--23

**Fixed omxyz current layer:**

Identify a hotel in Tokyo with a spa and wellness center, rated 9 or above, with availability for a five-night stay starting on June 20, 2026. Check if free cancellation is offered.

**Evaluated:**

Identify a hotel in Tokyo with a spa and wellness center, rated 9 or above, with availability for a five-night stay starting on December 12, 2026. Check if free cancellation is offered.

### Google Flights--21

**Fixed omxyz current layer:**

Locate the lowest-priced one-way flight from Tokyo to Sydney for an adult, departing o6 July 25, 2026, and include the flight duration and number of layovers.

**Evaluated:**

Locate the lowest-priced one-way flight from Tokyo to Sydney for an adult, departing o6 January 16, 2027, and include the flight duration and number of layovers.

### Booking--24

**Fixed omxyz current layer:**

Find a hotel in Barcelona for a stay from February 25-28, 2027. Please sort the results by distance from the beach and make sure they offer free Wi-Fi and breakfast.

**Evaluated:**

Find a hotel in Barcelona for a stay from February 25, 2027 to February 28, 2027. Please sort the results by distance from the beach and make sure they offer free Wi-Fi and breakfast.

### Google Flights--22

**Fixed omxyz current layer:**

Find a round-trip flight from Rio de Janeiro to Los Angeles, leaving on June 15, 2026, and returning on June 22, 2026, and select the option with the least carbon dioxide emissions.

**Evaluated:**

Find a round-trip flight from Rio de Janeiro to Los Angeles, leaving on December 7, 2026, and returning on December 14, 2026, and select the option with the least carbon dioxide emissions.

### Booking--25

**Fixed omxyz current layer:**

Search for a hotel in Lisbon with airport shuttle, rated 8.5 or above, available for a six-night stay from August 1 to August 7, 2026, for two adults, breakfast included.

**Evaluated:**

Search for a hotel in Lisbon with airport shuttle, rated 8.5 or above, available for a six-night stay from January 23, 2027 to January 29, 2027, for two adults, breakfast included.

### Google Flights--23

**Fixed omxyz current layer:**

Search for a one-way flight from Mumbai to Vancouver on July 28, 2026, filtering the results to show only 1-stop flights.

**Evaluated:**

Search for a one-way flight from Mumbai to Vancouver on January 19, 2027, filtering the results to show only 1-stop flights.

### Booking--26

**Fixed omxyz current layer:**

Check Booking.com for a 3-star hotel or higher in Paris with a guest rating above 8.0 and available parking for dates July 20-23, 2026.

**Evaluated:**

Check Booking.com for a 3-star hotel or higher in Paris with a guest rating above 8.0 and available parking for dates January 11, 2027 to January 14, 2027.

### Google Flights--24

**Fixed omxyz current layer:**

Compare prices for economy class round-trip flights from Dubai to Rome, departing on July 1, 2026, and returning on July 8, 2026, and select the option with the fewest stops.

**Evaluated:**

Compare prices for economy class round-trip flights from Dubai to Rome, departing on December 23, 2026, and returning on December 30, 2026, and select the option with the fewest stops.

### Booking--27

**Fixed omxyz current layer:**

Locate a hotel in Melbourne offering free parking and free WiFi, for a stay from June 28 to July 4, 2026.

**Evaluated:**

Locate a hotel in Melbourne offering free parking and free WiFi, for a stay from December 20, 2026 to December 26, 2026.

### Google Flights--25

**Fixed omxyz current layer:**

Find a one-way business class flight from Buenos Aires to Amsterdam on July 10, 2026, and provide the details of the flight with the shortest duration.

**Evaluated:**

Find a one-way business class flight from Buenos Aires to Amsterdam on January 1, 2027, and provide the details of the flight with the shortest duration.

### Booking--28

**Fixed omxyz current layer:**

Find a hotel in Dubai with a swimming pool, for a week-long stay from June 22 to June 29, 2026.

**Evaluated:**

Find a hotel in Dubai with a swimming pool, for a week-long stay from December 14, 2026 to December 21, 2026.

### Google Flights--26

**Fixed omxyz current layer:**

Search for the cheapest round-trip flights from Bangkok to Madrid, leaving on July 26, 2026, and returning on July 28, 2026, and provide options under $1000.

**Evaluated:**

Search for the cheapest round-trip flights from Bangkok to Madrid, leaving on January 17, 2027, and returning on January 19, 2027, and provide options under $1000.

### Booking--29

**Fixed omxyz current layer:**

Search for a hotel in Toronto with a fitness center and a rating of 8+, available for a two-night stay from July 5 to July 7, 2026.

**Evaluated:**

Search for a hotel in Toronto with a fitness center and a rating of 8+, available for a two-night stay from December 27, 2026 to December 29, 2026.

### Google Flights--27

**Fixed omxyz current layer:**

Locate a one-way flight from Johannesburg to Toronto on July 30, 2026, for one adult, and analyze the price trends for the following month.

**Evaluated:**

Locate a one-way flight from Johannesburg to Toronto on January 21, 2027, for one adult, and analyze the price trends for the following month.

### Booking--30

**Fixed omxyz current layer:**

Search for hotels in London from July 20 to July 23, 2026, on Booking. How many hotels are left after applying the Breakfast included and Fitness center filters?

**Evaluated:**

Search for hotels in London from January 11, 2027 to January 14, 2027, on Booking. How many hotels are left after applying the Breakfast included and Fitness center filters?

### Google Flights--28

**Fixed omxyz current layer:**

Find the best-priced round-trip flight from Seattle to Paris, departing on July 27, 2026, and returning on August 1, 2026, with a maximum of one stop.

**Evaluated:**

Find the best-priced round-trip flight from Seattle to Paris, departing on January 18, 2027, and returning on January 23, 2027, with a maximum of one stop.

### Booking--31

**Fixed omxyz current layer:**

Search for hotels in Rio de Janeiro from July 1-7, 2026, check the Brands filter to see which brand has the most hotels and which brand has the fewest.

**Evaluated:**

Search for hotels in Rio de Janeiro from December 23, 2026 to December 29, 2026, check the Brands filter to see which brand has the most hotels and which brand has the fewest.

### Google Flights--29

**Fixed omxyz current layer:**

Compare the prices and total travel time of non-stop flights from Mexico City to Frankfurt, departing on July 5, 2026, and returning on July 15, 2026.

**Evaluated:**

Compare the prices and total travel time of non-stop flights from Mexico City to Frankfurt, departing on December 27, 2026, and returning on January 6, 2027.

### Booking--32

**Fixed omxyz current layer:**

Look for hotels in Sydney from February 24 to February 27, 2027, on Booking. Once the Swimming Pool and Airport Shuttle filters are applied, what is the total number of hotels available?

**Evaluated:**

Look for hotels in Sydney from February 24, 2027 to February 27, 2027, on Booking. Once the Swimming Pool and Airport Shuttle filters are applied, what is the total number of hotels available?

### Google Flights--30

**Fixed omxyz current layer:**

Find the most affordable one-way flight from Cape Town to Singapore, departing on July 20, 2026, and include the airline and total number of layovers.

**Evaluated:**

Find the most affordable one-way flight from Cape Town to Singapore, departing on January 11, 2027, and include the airline and total number of layovers.

### Google Flights--31

**Fixed omxyz current layer:**

Find a one-way economy flight from Auckland to Honolulu on July 25, 2026, browse the full page and display a flight option with the most stops.

**Evaluated:**

Find a one-way economy flight from Auckland to Honolulu on January 16, 2027, browse the full page and display a flight option with the most stops.

### Booking--34

**Fixed omxyz current layer:**

Search for a hotel in Berlin available for a three-night stay from July 15 to July 18, 2026, for one adult. Tell me the price in USD and CNY for the three-night stay.

**Evaluated:**

Search for a hotel in Berlin available for a three-night stay from January 6, 2027 to January 9, 2027, for one adult. Tell me the price in USD and CNY for the three-night stay.

### Google Flights--32

**Fixed omxyz current layer:**

Search for round-trip flights from Stockholm to Toronto, departing on July 3, 2026, and returning on July 10, 2026, and sort the results to find the shortest total travel time.

**Evaluated:**

Search for round-trip flights from Stockholm to Toronto, departing on December 25, 2026, and returning on January 1, 2027, and sort the results to find the shortest total travel time.

### Google Flights--33

**Fixed omxyz current layer:**

Find a one-way flight from Shanghai to Vancouver on July 27, 2026, and compare the options based on carbon dioxide emissions.

**Evaluated:**

Find a one-way flight from Shanghai to Vancouver on January 18, 2027, and compare the options based on carbon dioxide emissions.

### Booking--36

**Fixed omxyz current layer:**

Search for a budget hotel in Rome under $100 per night for one adult from July 20 to July 23, 2026. Sort the results by price, identify if any of top three results offer breakfast.

**Evaluated:**

Search for a budget hotel in Rome under $100 per night for one adult from January 11, 2027 to January 14, 2027. Sort the results by price, identify if any of top three results offer breakfast.

### Google Flights--34

**Fixed omxyz current layer:**

Compare business class flight options from Lisbon to Singapore for a one-way trip on July 15, 2026, select one of the flights and see which websites offer its booking options. Which one is the cheapest.

**Evaluated:**

Compare business class flight options from Lisbon to Singapore for a one-way trip on January 6, 2027, select one of the flights and see which websites offer its booking options. Which one is the cheapest.

### Booking--37

**Fixed omxyz current layer:**

Search for a resort (not hotel) in Bali, detailing the available dates between July 20, 2026, and July 25, 2026, and checking any provided tour or cultural experiences.

**Evaluated:**

Search for a resort (not hotel) in Bali, detailing the available dates between January 11, 2027, and January 16, 2027, and checking any provided tour or cultural experiences.

### Google Flights--35

**Fixed omxyz current layer:**

Find the lowest-priced one-way flight from Cairo to Montreal on July 21, 2026, including the total travel time and number of stops.

**Evaluated:**

Find the lowest-priced one-way flight from Cairo to Montreal on January 12, 2027, including the total travel time and number of stops.

### Booking--38

**Fixed omxyz current layer:**

Look up Vienna hotel options with availability for a 4-night stay from June 28 to July 2, 2026, with amenities that include a Parking, breakfast included, and a rating of 8+ on Booking.com.

**Evaluated:**

Look up Vienna hotel options with availability for a 4-night stay from December 20, 2026 to December 24, 2026, with amenities that include a Parking, breakfast included, and a rating of 8+ on Booking.com.

### Google Flights--36

**Fixed omxyz current layer:**

Search for round-trip flights from Helsinki to New Delhi, departing on July 28, 2026, and returning on August 4, 2026, and filter the results to show only flights under $1000.

**Evaluated:**

Search for round-trip flights from Helsinki to New Delhi, departing on January 19, 2027, and returning on January 26, 2027, and filter the results to show only flights under $1000.

### Booking--39

**Fixed omxyz current layer:**

Find a pet-friendly hotel with parking available in downtown Toronto for the stay of July 24-26, 2026.

**Evaluated:**

Find a pet-friendly hotel with parking available in downtown Toronto for the stay of January 15, 2027 to January 17, 2027.

### Google Flights--37

**Fixed omxyz current layer:**

Locate a round-trip flight from Buenos Aires to Beijing, leaving on June 28, 2026, and returning on July 3, 2026, check out one of the options and tell me if the airline for my return flight is the same as my departure flight.

**Evaluated:**

Locate a round-trip flight from Buenos Aires to Beijing, leaving on December 20, 2026, and returning on December 25, 2026, check out one of the options and tell me if the airline for my return flight is the same as my departure flight.

### Booking--40

**Fixed omxyz current layer:**

I need to choose a hotel in Shenzhen, please select date (6 July to 8 July 2026) and click the search button. How much it costs when convert the price to Chinese Yuan on the page.

**Evaluated:**

I need to choose a hotel in Shenzhen, please select date (December 28, 2026 to December 30, 2026) and click the search button. How much it costs when convert the price to Chinese Yuan on the page.

### Google Flights--38

**Fixed omxyz current layer:**

Compare the prices and flight durations for economy class flights from Oslo to Dubai, departing on July 8, 2026, and show the options with no more than two layovers.

**Evaluated:**

Compare the prices and flight durations for economy class flights from Oslo to Dubai, departing on December 30, 2026, and show the options with no more than two layovers.

### Google Flights--39

**Fixed omxyz current layer:**

Find a one-way flight from Prague to a city in Japan on July 20, 2026, which city in Japan is cheaper to go to, Tokyo or a certain city in Hokkaido?

**Evaluated:**

Find a one-way flight from Prague to a city in Japan on January 11, 2027, which city in Japan is cheaper to go to, Tokyo or a certain city in Hokkaido?

### Booking--42

**Fixed omxyz current layer:**

Search for a hotel in Hokkaido for the period July 1 to July 7, 2026, with a rating of 9+, check out its user reviews, which categories are greater than 9 and which are less than 9?

**Evaluated:**

Search for a hotel in Hokkaido for the period December 23, 2026 to December 29, 2026, with a rating of 9+, check out its user reviews, which categories are greater than 9 and which are less than 9?

### Google Flights--41

**Fixed omxyz current layer:**

Choose one way business class ticket from Hong Kong to Glacier National Park on 6 July 2026, offering a 1 stop ticket.

**Evaluated:**

Choose one way business class ticket from Hong Kong to Glacier National Park on December 28, 2026, offering a 1 stop ticket.

