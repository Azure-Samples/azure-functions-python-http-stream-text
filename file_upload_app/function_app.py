import azure.functions as func
import os

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="streaming_upload", methods=[func.HttpMethod.POST])
def main(req: func.HttpRequest) -> func.HttpResponse:
    req_body = req.get_body()
    file_path = "hello_world.txt"
    if not file_path:
        return func.HttpResponse(
            "Please provide a 'file_path' parameter in the request URL.",
            status_code=400
        )
    if not os.path.exists(file_path):
        return func.HttpResponse(
            "The specified file path does not exist.",
            status_code=400
        )

    with open(file_path, 'rb') as file:
        data = file.read()
        process_data(data)

    return func.HttpResponse("Data uploaded and processed successfully", status_code=200)

def process_data(data: bytes):
    print(f"Processing {len(data)} bytes of data")