import azure.functions as func
import logging
import datetime
import requests
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

        
@app.function_name(name="pogodynka")
@app.timer_trigger(schedule="* * * * *", 
              arg_name="mytimer",
              run_on_startup=True) 
def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    
    url = "https://demopogodowe-ftd4fvfecbe0bkfx.polandcentral-01.azurewebsites.net/raw/warsaw"
    
    try:
        response = requests.post(url)
        logging.info(f"POST request sent. Status Code: {response.status_code}, Response: {response.text}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error sending POST request: {e}")
