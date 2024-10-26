from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
import time
from openai import OpenAI
import os

ENDPOINT = os.getenv("AZURE_OCR_ENDPOINT")
KEY = os.getenv("AZURE_OCR_KEY")
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")

client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))
open_ai_client = OpenAI(
    api_key=OPEN_AI_KEY,
)

def categorize_items(item_list):
    prompt = (
        "Categorize the following items into 'Rooms' and 'Electrical Equipment' and attempt to fix the spelling if required:\n"
        + "\n".join(item_list)
    )

    response = open_ai_client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

def recognize_text_with_correction(read_image_path):
    read_image = open(read_image_path, "rb")

    read_response = client.read_in_stream(read_image, raw=True)
    read_operation_location = read_response.headers["Operation-Location"]
    operation_id = read_operation_location.split("/")[-1]

    while True:
        read_result = client.get_read_result(operation_id)
        if read_result.status.lower () not in ['notstarted', 'running']:
            break
        print ('Waiting for result...')
        time.sleep(10)

    items = []
    if read_result.status == OperationStatusCodes.succeeded:
        for text_result in read_result.analyze_result.read_results:
            for line in text_result.lines:
                print(line.text + " at location: " + str(line.bounding_box))
                items.append(line.text)
    print()

    output = categorize_items(items)
    print("Categorized Output:" + output)

def main():
    original_image_path = "house_plan.jpg" 
    recognize_text_with_correction(original_image_path)

if __name__ == "__main__":
    main()
