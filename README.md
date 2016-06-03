TIH is an intelligence tool that helps you in searching for IOCs across multiple openly available security feeds and some well known APIs. The idea behind the tool is to facilitate searching and storing of frequently added IOCs for creating your own set of indicators.

#Threat-Intelligence-Hunter

####Summary
TIH is an intelligence tool that helps you in searching for IOCs across multiple openly available security feeds and some well known APIs. The idea behind the tool is to facilitate searching and storing of frequently added IOCs for creating your own set of indicators.

Requirements
----
* Python 2.7
* Argparse
* Urllib2
* Re
* API keys from Virustotal and URLVoid

Features
----
*Local storage of threat feeds

This allows you to regularly update your local storage from listed feeds under feeds.py. You can add your own favourite list if it is missing from the list. 
```
python tih.py -update
```

*check an IP against existing threat feeds and your local database

```
python tih.py -ip <IP Address to lookup>
```
*check for Bulk IP address list(in a text file)

```
python tih.py -list <file.txt>
```

*Check for MD5 Hash

```
python tih.py -md5 <hash>
```

*Check URL for blacklisting

```
python tih.py -url <your_url>
```

*Check for IP/URL reputation (Currently supports URLVoid and Virustotal)
Before using this feature, make sure you have added your public keys for URLVoid and VT to ```urlvoid.py``` and ```vt.py``` respectively.

```
python tih.py -repo <URL/IP>
```

<b><i>Final Version -></b></i>
<b>Darklord</b>
<p>No more limits. Keep adding your updates and changes</p>

<b><i>Previous Version -></b></i> 
<b><i>Bellatrix Lestrange</b></i>
<p>This version will have a more organized output and search mechanism.</p> 

<b><i>Current version -> </b></i>
<b>Peter Pettigrew v0.8</b>
<p>This version adds support for local storage of feeds.</p>

<b><i>Previous versions -> </b></i>

<b>Rita Skeeter v0.6</b>
<p>This version will have support for domains as indicators. </p>
<b>Lucious Malfoy v0.4</b>
<p>This version will have support for MD5 as Commandline input as well as a list inside a TXT file.</p>
<b>Draco Malfoy v0.2.</b>
<p>Now supports a list of IP addresses as indicators.
Supports Single or multiple IPs as commandline arguments and parses it against a list of indicators.</p>
