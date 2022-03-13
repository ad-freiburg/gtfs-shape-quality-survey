import urllib.request
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: " + sys.argv[0] + " <OUT_FOLDER>")
        exit(1)
    out_dir = sys.argv[1]
    for line in sys.stdin:
        parts = line.split(';')

        url = "https://openmobilitydata.org/p/" + parts[1] + "/download"

        req = urllib.request.Request(
            url,
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )

        print("Fetching " + parts[0]);

        try:
            data = urllib.request.urlopen(req).read()
            f = open("feeds/" + parts[0].replace("/", "_") + ".zip", "wb")
            f.write(data)
            f.close()

        except urllib.error.HTTPError as e:
            print(e)

if __name__ == "__main__":
    main()
