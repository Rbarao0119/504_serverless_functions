import json
import functions_framework

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Expects JSON with 'a1c' (or query param as fallback).
    Returns a JSON classification of A1C levels.
    """
    # Prefer JSON body; fall back to query parameters for convenience
    data = request.get_json(silent=True) or {}
    args = request.args or {}

    a1c = data.get("a1c", args.get("a1c"))

    # Presence check
    if a1c is None:
        return (
            json.dumps({"error": "Field 'a1c' is required."}),
            400,
            {"Content-Type": "application/json"},
        )

    # Type/convert check
    try:
        a1c_val = float(a1c)
    except (TypeError, ValueError):
        return (
            json.dumps({"error": "'a1c' must be a number (e.g., 5.6)."}),
            400,
            {"Content-Type": "application/json"},
        )

    # Classification
    if a1c_val < 5.7:
        status = "healthy"
        category = "Healthy (<5.7%)"
    elif 5.7 <= a1c_val <= 6.4:
        status = "prediabetes"
        category = "Prediabetes (5.7%–6.4%)"
    else:
        status = "diabetes-range"
        category = "Diabetes-range (≥6.5%)"

    payload = {
        "a1c": a1c_val,
        "status": status,
        "category": category,
    }

    return json.dumps(payload), 200, {"Content-Type": "application/json"}
