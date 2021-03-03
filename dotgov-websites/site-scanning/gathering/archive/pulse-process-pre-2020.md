
Before pulse.cio.gov was decommissioned, here's the process it would use to generate a Target URL List.  

Summary: 

* The Pulse program would initiate.  
* Pulse would then employ the domain-scan application to gather a number of specific datasets, process them, and assemble them into one Target URL list.  
* Pulse would specify which sources of data to gather [here](https://github.com/18F/pulse/blob/master/data/env.py#L42-L53).  
* Pulse would give the location for each dataset that was to be gathered [here](https://github.com/18F/pulse/blob/master/meta.yml#L10-L34).
* Once each dataset was gathered, they would be processed (remove www., etc) using instructions set out [here](https://github.com/18F/domain-scan/blob/master/gather).  

Note: At an earlier date, the ability to query the Censys and RDNS datasets directly (instead of using a snapshot CSV file) were operated using these gathering files: [Censys](https://github.com/18F/domain-scan/blob/master/gatherers/censys.py) | [RDNS](https://github.com/18F/domain-scan/blob/master/gatherers/rdns.py).  
