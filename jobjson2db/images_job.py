from handlers.image_handler import ImageHandler
from datetime import datetime
import schedule
import time
import json
import os


def main():
    FROM_PATH = "./images/"
    TO_PATH = "./images_ok/"
    ERROR_PATH = "./images_error/"
    LOG_PATH = "./images_log/"
    JSON_PATH = "./jsons/"
    
    images = os.listdir(FROM_PATH)
    for image in images:
        log_file = image[:image.index(".")] + datetime.now().strftime("_%Y_%m_%d_%H_%M_%S") + ".txt"
        json_file = image[:image.index(".")] + ".json"
        response = ImageHandler.open(FROM_PATH + image)
        if not response.successed:
            os.rename(FROM_PATH + image, ERROR_PATH + image)
            with open(LOG_PATH + log_file, "w") as f:
                f.write(f"[ERROR] {response.error_msg}")
            continue
                
        response = ImageHandler.count(response.data)
        if not response.successed:
            os.rename(FROM_PATH + image, ERROR_PATH + image)
            with open(LOG_PATH + log_file, "w") as f:
                f.write(f"[ERROR] {response.error_msg}")
            continue
        
        os.rename(FROM_PATH + image, TO_PATH + image)
        
        with open(JSON_PATH + json_file, "w") as f:
            json.dump(response.data, f)
        

if __name__ == "__main__":
    schedule.every(15).seconds.do(main)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        print("Rodou!")