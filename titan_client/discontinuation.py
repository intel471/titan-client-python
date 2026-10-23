import logging

log = logging.getLogger("titan_client")

DISCONTINUATION_MESSAGE = (
    "Titan access is being discontinued. Access to TITAN, including UI and API, will soon be discontinued. "
    "Please review and complete any outstanding migration tasks before access ends. "
    "If you require assistance or have any questions, your CM or the Intel 471 Support Team "
    "(support@intel471.com) are available to help."
)


def warn_discontinuation():
    log.warning(DISCONTINUATION_MESSAGE)
