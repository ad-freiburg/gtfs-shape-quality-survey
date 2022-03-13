import urllib.request
import json
import sys

# march 2020
# t = 1583047396

def main():
    args = dict(zip(*[iter(sys.argv[1:])]*2))

    if not "--api-key" in args or not "--end-time" in args:
        sys.stderr.write("Usage: " + sys.argv[0] + " --api-key <TRANSITFEEDS-API-KEY> --end-time <UNIX TS>\n")
        exit(1)

    api_key = args["--api-key"] #"273110fa-470f-4312-a540-5fd1c9d2b328"
    t = int(args["--end-time"]) #1583047396

    this_page = 1
    tot_pages = 1

    feeds = {}

    while this_page <= tot_pages:
        try:
            with urllib.request.urlopen("https://api.transitfeeds.com/v1/getFeedVersions?key=" + api_key + "&page=" + str(this_page) + "&limit=100&err=1&warn=1") as url:
                data = json.loads(url.read().decode())

                tot_pages = int(data["results"]["numPages"])
                this_page = int(data["results"]["page"])

                this_page = this_page + 1

                for ver in data["results"]["versions"]:
                    ver_id = ver["id"]
                    feed_id = ver["f"]["id"]
                    ts = int(ver["ts"])

                    if ts > t:
                        continue

                    if feed_id not in feeds or ts > feeds[feed_id]["ts"]:
                        feeds[feed_id] = {"ver_id" : ver_id, "ts" : ts}

        except urllib.error.HTTPError as e:
            this_page = this_page + 1

    for feed_id in feeds:
        print(feed_id + ";" + feeds[feed_id]["ver_id"] + ";" + str(feeds[feed_id]["ts"]))


if __name__ == "__main__":
    main()
