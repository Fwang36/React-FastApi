import sentry_sdk
import time

@sentry_sdk.trace
def func5():
    time.sleep(3)
    return "func5"



