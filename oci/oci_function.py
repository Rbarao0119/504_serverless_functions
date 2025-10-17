import io
import json
import logging
from fdk import response

def handler(ctx, data: io.BytesIO = None):
    a1c = None
    try:
        body = json.loads(data.getvalue())
        a1c = body.get("a1c")
    except (Exception, ValueError) as ex:
        logging.getLogger().info("error parsing json payload: " + str(ex))

    logging.getLogger().info("Inside A1C classification function")

    if a1c is None:
        result = {"error": "Please provide 'a1c' in JSON, e.g. {'a1c': 6.2}"}
    else:
        try:
            a1c = float(a1c)
            if a1c < 5.7:
                category = "normal"
            elif a1c < 6.5:
                category = "prediabetes"
            else:
                category = "diabetes"

            eAG = 28.7 * a1c - 46.7  # estimated average glucose
            result = {
                "a1c": a1c,
                "category": category,
                "eAG_mg_dL": round(eAG, 1)
            }
        except Exception as ex:
            result = {"error": "Invalid 'a1c' value", "detail": str(ex)}

    return response.Response(
        ctx,
        response_data=json.dumps(result),
        headers={"Content-Type": "application/json"}
    )
