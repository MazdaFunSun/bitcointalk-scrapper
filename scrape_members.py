""" Core scraper for bitcointalk.org. """
import bitcointalk
import logging
import memoizer
import os
import sys
import traceback

startMemberId = 1
stopMemberId = 500000

logging.basicConfig(
    filename='scraper.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p')

# Make sure we don't rescrape information already in the DB
memoizer.remember()

for memberId in range(startMemberId, stopMemberId+1):
    logging.info(">Starting scrape of topic ID {0}...".format(memberId))
    try:
        member = memoizer.scrapeMember(memberId)

    except Exception as e:
	exc_type, exc_value, exc_traceback = sys.exc_info()
        print '-'*60
        print "Could not request URL for member {0}:".format(memberId)
        print traceback.format_exc()
        print '-'*60
        logging.warning(">Could not request URL for member {0}:{1}{2},".format(memberId,exc_type, exc_value))
        continue
logging.info("All done.")
logging.info("Made {0} requests in total.".format(bitcointalk.countRequested))
