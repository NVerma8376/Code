from pyttsx3.drivers.espeak import EspeakDriver
import logging

def setup_espeak_driver():
    try:
        driver = EspeakDriver()
        # Set up the driver...
        return driver
    except Exception as e:
        logging.error(f"Failed to initialize EspeakDriver: {str(e)}")
        return None

# Usage
driver = setup_espeak_driver()
if driver:
    try:
        driver.say("Hello, world!")
    except ReferenceError:
        logging.warning("EspeakDriver was garbage collected while speaking.")
    finally:
        driver.stop()
        driver.shutdown()
else:
    print("Couldn't set up EspeakDriver. Using alternative method...")
