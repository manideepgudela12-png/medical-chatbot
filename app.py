from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 20 medicines
medicines = {
    "paracetamol": "Uses: Reduces fever and mild pain.<br>Side Effects: Rare allergic reaction.<br>Precautions: Do not overdose.",
    "ibuprofen": "Uses: Reduces inflammation and pain.<br>Side Effects: Stomach upset.<br>Precautions: Take with food.",
    "amoxicillin": "Uses: Antibiotic for infections.<br>Side Effects: Nausea, diarrhea.<br>Precautions: Complete the course.",
    "lisinopril": "Uses: Lowers blood pressure.<br>Side Effects: Dizziness.<br>Precautions: Monitor BP regularly.",
    "atorvastatin": "Uses: Lowers cholesterol.<br>Side Effects: Muscle pain.<br>Precautions: Avoid grapefruit.",
    "omeprazole": "Uses: Reduces stomach acid.<br>Side Effects: Headache.<br>Precautions: Take before meals.",
    "salbutamol": "Uses: Relieves asthma symptoms.<br>Side Effects: Tremors, palpitations.<br>Precautions: Follow dosage.",
    "metformin": "Uses: Controls blood sugar.<br>Side Effects: Nausea, stomach upset.<br>Precautions: Take with meals.",
    "cetirizine": "Uses: Allergy relief.<br>Side Effects: Drowsiness.<br>Precautions: Avoid alcohol.",
    "prednisone": "Uses: Reduces inflammation.<br>Side Effects: Weight gain, mood changes.<br>Precautions: Take as prescribed.",
    "loratadine": "Uses: Allergy relief.<br>Side Effects: Rare, headache.<br>Precautions: Safe for most adults.",
    "azithromycin": "Uses: Antibiotic for infections.<br>Side Effects: Stomach upset.<br>Precautions: Complete full course.",
    "hydrochlorothiazide": "Uses: Diuretic for high BP.<br>Side Effects: Frequent urination.<br>Precautions: Monitor electrolytes.",
    "gabapentin": "Uses: Nerve pain relief.<br>Side Effects: Dizziness, drowsiness.<br>Precautions: Avoid driving initially.",
    "simvastatin": "Uses: Lowers cholesterol.<br>Side Effects: Muscle pain.<br>Precautions: Avoid grapefruit.",
    "fluoxetine": "Uses: Treats depression.<br>Side Effects: Nausea, headache.<br>Precautions: May take 2-4 weeks to work.",
    "clindamycin": "Uses: Antibiotic for infections.<br>Side Effects: Diarrhea.<br>Precautions: Complete full course.",
    "allopurinol": "Uses: Treats gout.<br>Side Effects: Rash, nausea.<br>Precautions: Take after meals.",
    "warfarin": "Uses: Blood thinner.<br>Side Effects: Bleeding.<br>Precautions: Monitor INR.",
    "furosemide": "Uses: Diuretic for fluid retention.<br>Side Effects: Frequent urination.<br>Precautions: Take in morning."
}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form.get("medicine", "").lower()
        return redirect(url_for("home", medicine=user_input))

    user_input = request.args.get("medicine", "").lower()
    if user_input:
        result = medicines.get(user_input, "Medicine not found in database.")
        user_message = user_input
    else:
        result = None
        user_message = None

    return render_template("index.html", result=result, user_message=user_message)

if __name__ == "__main__":
    app.run(debug=True)
