from agent import graph

@app.route("/run_agent/<district_id>")
def run_agent(district_id):

    result = graph.invoke({
        "district_id": district_id,
        "data": {},
        "analysis": "",
        "scenarios": [],
        "validation": "",
        "history": []
    })

    return result