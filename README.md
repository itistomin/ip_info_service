# IP Info Service

# Common Info

This service provides and information about the IP address of the client.
It can return location info (city, country), timezone, latitude and longitude, zip code, etc.

There are two endpoints available:
1. `/me` - returns info about the IP address of the client. Note that localhost is also supported, and will return empty data.
2. `/<ip>` - returns info about the provided IP address.

If IP is not in the database, server raises HTTP 404 error.

Usage example:
```bash
    curl http://localhost:8000/me/
```

```bash
    curl http://localhost:8000/19.18.123.5/
```

# Run locally

!Note: Put IP2LOCATION-LITE-DB11.CSV file into `src/artifacts` folder before running the server.
Git does not allow to upload files bigger than 100MB, so I had to remove it from the repo.
Download link: https://lite.ip2location.com/download?id=9


To run application locally, you need to have Python 3.10+ installed.
1. Create a vitualenv and activate it:
```bash
    python3 -m venv venv
    source venv/bin/activate
```

2. Install dependencies:
```bash
    pip install -r requirements.txt
```

3. Run the server:
```bash
    uvicorn main:app --reload
```

Note: you may need to export PYTHONPATH=/path/to/project/src (e.g `export PYTHONPATH=/home/user/ip-info-service/src`) to run the server.

Server should be available at http://localhost:8000/
Documentation should be available at http://localhost:8000/docs/

Note: database file is big, and on start/restart server needs 5-10 seconds to load it.
