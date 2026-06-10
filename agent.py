import json
from datetime import datetime


def web_search(query):
    return [
        {
            "title": "Result 1",
            "content": f"Information about {query}"
        },
        {
            "title": "Result 2",
            "content": f"Latest updates regarding {query}"
        },
        {
            "title": "Result 3",
            "content": f"Important facts related to {query}"
        }
    ]


def generate_response(query, search_results):
    summary = f"\nSummary for '{query}':\n\n"

    for i, result in enumerate(search_results, start=1):
        summary += f"{i}. {result['content']}\n"

    return summary


def save_query(query):
    data = {
        "query": query,
        "created_at": str(datetime.now())
    }

    with open("memory.json", "w") as f:
        json.dump(data, f)


def run_agent(query):
    results = web_search(query)

    answer = generate_response(query, results)

    save_query(query)

    print(answer)


if __name__ == "__main__":
    query = input("Ask something: ")
    run_agent(query)