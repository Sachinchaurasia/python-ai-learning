import json

data={
    "topic":"Embedding",
    "difficulty":"Beginner",
    "definition":"A numerical representation of information",
    "use-cases":
        [
            "Semantic Search",
            "RAG",
            "Recommendation System"
        ]
}

json_data=json.dumps(data,indent=4)
print(json_data)


#Read the data

print("\n topic:")
print(data["topic"])
print("\n difficulty:")
print("\n Use Cases:")

for use_cases in data["use-cases"]:
    print("-",use_cases)
    