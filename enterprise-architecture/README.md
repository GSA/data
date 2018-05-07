# GSA Enterprise Architecture

> The Enterprise Architecture, Policy and Planning Division provides business-focused IT support for GSA customers at all levels of the organization.

The General Services Administration's [Enterprise Architecture](http://www.gsa.gov/portal/category/26815) team maintains a list of systems approved for use at GSA, called the [IT Standards Profile list](it-standards.csv). This list includes:

* Desktop software
* Server software
* Software as a Service (SaaS)

Make sure to **pay attention to the `Status` column**, as the list includes items that are `Approved`, `Pending`, and `Denied` (though there can be other values for the column).

The data is manually exported (for now) from [the official list in GEAR](https://ea.gsa.gov/#!/itstandards) on a regular (but best-effort) basis. See the Last Modified date on the CSV to see when it was last updated. Feel free to [open an issue](https://github.com/GSA/data/issues/new) to give us a nudge if we forget!

To see the latest-and-greatest list, get on the GSA network (see [VPN information](https://handbook.18f.gov/anyconnect/)), and visit [GEAR](https://ea.gsa.gov/#!/itstandards).

## Updating the list

Requires:

* Being on the GSA network
* cURL
* Git
* Python 3

From this directory, run the updating script:

```sh
./update.sh
```
