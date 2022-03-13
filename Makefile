API_KEY = ENTER_YOUR_API_KEY

%.list:
	@echo "Fetching feed ids for $*"
	@python3 fetch_ids.py --api-key $(API_KEY) --end-time `date -d '$*-03-01 00:00:00 GMT' +%s` > $@

feeds/%: %.list
	@mkdir -p $@
	@python3 fetch_feeds.py $@ < $<

%.res: feeds/%
	@gtfs-shp-eval $< > $@
	@echo "\n*******************"
	@echo Finished evaluation for $*
	@echo "*******************\n"
	@cat $@

eval: | 2015.res

help:
	@cat README.md
