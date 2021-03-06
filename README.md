
Slack Status
============

A simple Python server for updating slack statuses over
multiple slack accounts based on location using IFTTT triggers.

Configuration
-------------

Locations and statuses are registered in `status.py`. Each supported
location should have a dictionary with slack accounts as keys and a 
status tuple (`emoji_name`,`status_text`) as the values. 

**Note:** Custom emojis can be used. However if an account does not
  contain that emoji, the status update for that account will fail.

Every status dictionary should then be added to the locations
dictionary, which is used by the server to identify and set location
statuses.

### Locations

The `locations` dictionary in `status.py` defines a series of
locations where the keys are the name of a location and the values are
status dictionaries. Status dictionaries represent a set of actions
that should be taken for each of the accounts (the status dictionary
keys) in that dictionary. The status that will be set for the
corresponding account are the values of the status dictionary.

If an account is absent from a location dictionary, no action will be
taken to update the account's status.

### Aliases

If all of the statuses for one account should match another, an alias
entry can be provided in the `status.py` file as a key-value pair in
the aliases dictionary. The account name with existing entries in the
`locations` structure should be the value. The account mimicking the
existing account statuses should be the key.

```python
aliases = { 'account1_name' : 'account0_name' }
```

The server will read this as: "Treat `account1` as if it were `account0`".

Tokens
------

Tokens for any account in the `locations` or `alias` dictionaries
should be provided in this file. The file should contain a dictionary
named `tokens` formatted like so: 

```python
tokens = { 'account0_name' : TOKEN,
           'account1_name' : TOKEN }
```

For safety, it is best to keep 

Serving
-------

To start the server one can run

```shell
python server.py
```

which will start a server on port 8000 of the default IP address for
the machine in use.

The server IP address can also be configured using the `--IP` option
of this command.

Setting a Status
----------------

A status can be set by sending a GET request to a url with the format: 

```
https://<server_ip_address>/<location_name>
```

One can connect IFTTT by adding a webhook trigger based on their location
to ping the server.

Dependencies
------------

Python: 

`urllib2`, `SocketServer`, `SimpleHTTPServer`
