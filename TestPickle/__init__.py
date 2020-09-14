import logging
import json
import azure.functions as func

from .suggester import Suggester


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = req.params.get('data')
    if not data:
        try:
            req_body = req.get_json()
        except ValueError:
            return func.HttpResponse(
                json.dumps({
                    "success": False
            }))
        else:
            data = req_body.get('data')

    s = Suggester()
    suggested_features = s.suggest(data)
    
    return func.HttpResponse(
        json.dumps({
            "success": True,
            "data": suggested_features
        })
    )