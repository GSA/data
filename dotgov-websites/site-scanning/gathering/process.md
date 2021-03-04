

## Datasets
* [List of Federal .Gov Domains](https://github.com/GSA/data/blob/master/dotgov-domains/current-federal.csv) - ~1,200 records
* [List of Websites That Participate In The Digital Analytics Program](https://analytics.usa.gov/data/live/sites.csv) - ~5,700 records
* [2016 End of Term Web Archive](https://github.com/end-of-term/eot2016/blob/master/seed-lists/eot_2016_bulk_seeds_test_report.txt) - ~
* One Month of DNS Records from the .Gov Registry, 3rd Level Only (Link Coming) - ~10,000

## Process
* The above datasets are downloaded and a static copy is stored [in this repository](https://github.com/GSA/data/tree/master/dotgov-websites/site-scanning/gathering/data).  
* They are then combined and deduped.  



Questions:  
* do the columns need aligning? 
* what columns are removed?
* what structure (what fields, in what order, what formatting for each cell) do we want the final product to look like?  
* where do we want the final product to go?


## Other Potential Datasets

This is as a list of potential sources for data that can be used to assemble the `current-federal-subdomains.csv` file.  

* Censys
* Rapid7
* [2020 End of Term Web Archive](https://github.com/end-of-term/eot2016/blob/master/seed-lists/eot_2016_bulk_seeds_test_report.txt)
* [USA.gov's List of Federal Websites That Don't End In .Gov or .Mil](https://github.com/gsa/govt-urls)
* Search.gov Index
