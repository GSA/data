# .gov websites

This directory contains already trivially publicly discoverable `.gov` hostname data.

There are two new snapshots of federal `.gov` websites:

- A snapshot of a set of ~20,000 hostnames from a search in Censys, performed in late November 2017, filtered to `.gov` and `.fed.us` hostnames that are subdomains of federal `.gov` domains, and filtered to only hosts that responded to HTTP/HTTPS over the public internet. This is snapshotted here ahead of Censys changing their technical and business model on December 1st. We anticipate continuing to get data from Censys after December 1st, but also expect there to be a gap, during which we'll use this snapshot.

- A snapshot of a set of ~9,000 hostnames from Rapid7's Reverse DNS v2 dataset, fileted to `.gov` and .fed.us hostnames that are subdomains of federal `.gov` domains, and filtered to only hosts that responded to HTTP/HTTPS over the public internet. This is snapshotted here because getting this data in an automated, dynamic way is currently pretty difficult (due to Rapid7's full dataset being a single ~130GB file when unzipped). Until we've invested in a way to automate this effectively and cheaply, this snapshot can be updated whenever it's convenient and useful.

We are already providing a snapshot of ~194,000 hostnames in the End-of-Term Archive 2016 dataset, converted to CSV. These hostnames are not filtered from what the EOT provided, though since they principally derive domains from a web crawl, they should generally refer to web services and not other services. (Many are defunct, however.) This moves the EOT data into the same directory as the above snapshots, for consistency. (A copy is left in the old directory to provide some transition help for those using the old URL.)
