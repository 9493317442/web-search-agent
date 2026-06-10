import json
import schedule
import time

from agent import web_search, generate_response


def follow_up():
    with open("memory.json", "r") as f:
        data = json.load(f)

    query = data["query"]

    print("\nRunning follow-up search...")

    results = web_search(query)

    answer = generate_response(query, results)

    print("\nUpdated Response:")
    print(answer)


schedule.every(14).days.do(follow_up)

print("Scheduler Started...")

while True:
    schedule.run_pending()
    time.sleep(60)