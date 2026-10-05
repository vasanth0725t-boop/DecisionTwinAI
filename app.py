from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def create_future(option, decision):
    option_lower = option.lower()

    positive_words = [
        "learn", "study", "practice", "improve",
        "career", "skill", "project", "exercise"
    ]

    if any(word in option_lower for word in positive_words):
        result = (
            f"Choosing {option} can help you build useful skills "
            f"related to your decision: {decision}."
        )
        benefits = [
            "Can improve your skills",
            "Can create new opportunities",
            "Can provide practical experience"
        ]
        challenges = [
            "Requires regular effort",
            "Progress may take time",
            "You may need continuous practice"
        ]
    else:
        result = (
            f"If you choose {option}, your future may depend on "
            "your effort, consistency and situation."
        )
        benefits = [
            "May provide a different opportunity",
            "Can give you new experience",
            "Can help you explore another path"
        ]
        challenges = [
            "May involve uncertainty",
            "Requires commitment",
            "Results can vary"
        ]

    return {
        "option": option,
        "result": result,
        "benefits": benefits,
        "challenges": challenges
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/decide", methods=["POST"])
def decide():
    data = request.get_json()

    decision = data.get("decision", "").strip()
    option_a = data.get("option_a", "").strip()
    option_b = data.get("option_b", "").strip()

    if not decision or not option_a or not option_b:
        return jsonify({
            "error": "Please enter the decision and both options."
        }), 400

    future_a = create_future(option_a, decision)
    future_b = create_future(option_b, decision)

    comparison = (
        f"For your decision '{decision}', both options have possible "
        "benefits and challenges. Compare the two future paths based "
        "on your interests, goals and available time."
    )

    return jsonify({
        "decision": decision,
        "future_a": future_a,
        "future_b": future_b,
        "comparison": comparison
    })


if __name__ == "__main__":
    app.run(debug=True)
    