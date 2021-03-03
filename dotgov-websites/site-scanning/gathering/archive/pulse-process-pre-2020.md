
Before pulse.cio.gov was decommissioned, here's the process it would use to generate a Target URL List.  

#### Summary

* The Pulse program would initiate.  
* Pulse would then employ the domain-scan application to gather a number of specific datasets, process them, and assemble them into one Target URL list.  
* Pulse would specify which sources of data to gather [here](https://github.com/18F/pulse/blob/master/data/env.py#L42-L53).  
* Pulse would give the location for each dataset that was to be gathered [here](https://github.com/18F/pulse/blob/master/meta.yml#L10-L34).
* Once each dataset was gathered, they would be processed using instructions set out [here](https://github.com/18F/domain-scan/blob/master/gather) (see a summary of this below).  

Note: At an earlier date, we were able to query the live Censys and Rapid7 datasets directly (instead of using a static snapshot CSV as we later would).  This was done these gathering files: [Censys](https://github.com/18F/domain-scan/blob/master/gatherers/censys.py) | [Rapid7](https://github.com/18F/domain-scan/blob/master/gatherers/rdns.py).  


#### Further Details

Here is a rough summary at describing what was done during the processing stage:  

* Remove the protocol. 
* Cut naive wildcard prefixes out. (from certs)
* Cut off any redaction markers from names. (from certs)
* Check that the base domain (a.k.a. parent) of the entry was in the [canonical list of federal .gov domains](https://github.com/GSA/data/raw/master/dotgov-domains/current-federal.csv).  If it wasn't, it would be discarded.  This was useful in case one of the datasets had state/local .gov entries, or accidentally had non-governmental entries.  
* Finally, it would dedup the list.  
