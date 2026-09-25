def proposed_queue(answer, minimum_confidence):
    allowed = {"billing", "technical"}
    if answer["choice"] not in allowed:
        return "review"
    if answer["confidence"] < minimum_confidence:
        return "review"
    return answer["choice"]
