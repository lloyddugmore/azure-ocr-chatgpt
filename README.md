# OCR Azure and ChatGPT POC

This project is a proof of concept to demonstrate the integration of Azure OCR and ChatGPT to extract text from images and generate a summary of the extracted text.

## Installation

1. Clone the repository
2. Run docker-compose up

# Pre-requisites

1. Azure Cognitive Services key and endpoint for OCR, you can get it from [here](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/)
2. OpenAI API key for ChatGPT, you can get it from [here](https://beta.openai.com/signup/)

## Environment Variables

- `AZURE_OCR_ENDPOINT`: Azure Cognitive Services key
- `AZURE_OCR_KEY`: Azure Cognitive Services endpoint
- `OPEN_AI_KEY`: OpenAI API key

## Usage

Running docker-compose up will start the application.

The application will run and OCR the image provided along with the Repo and generate a summary of the extracted text.

`input`
![Alt text](house_plan.jpg?raw=true "House Plan")

`output`

```

ocr-poc-service  | Categorized Output:Rooms:
ocr-poc-service  | SAUNA
ocr-poc-service  | GYM
ocr-poc-service  | TREATMENT
ocr-poc-service  | ROOM
ocr-poc-service  | STORAGE
ocr-poc-service  | WINE STORE
ocr-poc-service  | BATHROOM (Fixed from BATHRM)
ocr-poc-service  | NEW 190 BLOCK WALL
ocr-poc-service  | STAIRS
ocr-poc-service  | NEW 240 BLOCK WALL
ocr-poc-service  |
ocr-poc-service  | Electrical Equipment:
ocr-poc-service  | ON SENSOR
ocr-poc-service  | Single gang switch
ocr-poc-service  | Double gang switch
ocr-poc-service  | Triple gang switch
ocr-poc-service  | Single two way switch
ocr-poc-service  | Double two way switch
ocr-poc-service  | Dimmer
ocr-poc-service  | Double dimmer
ocr-poc-service  | Sensor
ocr-poc-service  | Light inside cabinet
ocr-poc-service  | Wall light
ocr-poc-service  | Ceiling fan no light
ocr-poc-service  | Low level wall light
ocr-poc-service  | Pinhole recessed light
ocr-poc-service  | Recessed downlight
ocr-poc-service  | Lineal Pendant light
ocr-poc-service  | Pendant light
ocr-poc-service  | Ceiling Extraction fan
ocr-poc-service  | LED under cabinet
ocr-poc-service  | LED Wall wash/Bulkhead
ocr-poc-service  | LED under bathroom vanity
ocr-poc-service  | LED around Mirror
ocr-poc-service  | Wall light Exterior
ocr-poc-service  | Exterior wall spot
ocr-poc-service  | Exterior downlight
ocr-poc-service  | Triple two way switch
```
