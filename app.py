from flask import Flask, render_template, request, Response
from src.Pipelines.Prediction_Pipeline import USvisaData, USvisaClassifier

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("usvisa.html", context="Rendering")

@app.route("/", methods=["POST"])
def predict_route_client():
    try:
        continent = request.form.get("continent")
        education_of_employee = request.form.get("education_of_employee")
        has_job_experience = request.form.get("has_job_experience")
        requires_job_training = request.form.get("requires_job_training")
        no_of_employees = request.form.get("no_of_employees")
        company_age = request.form.get("company_age")
        region_of_employment = request.form.get("region_of_employment")
        prevailing_wage = request.form.get("prevailing_wage")
        unit_of_wage = request.form.get("unit_of_wage")
        full_time_position = request.form.get("full_time_position")

        usvisa_data = USvisaData(
            continent=continent,
            education_of_employee=education_of_employee,
            has_job_experience=has_job_experience,
            requires_job_training=requires_job_training,
            no_of_employees=no_of_employees,
            company_age=company_age,
            region_of_employment=region_of_employment,
            prevailing_wage=prevailing_wage,
            unit_of_wage=unit_of_wage,
            full_time_position=full_time_position,
        )

        usvisa_df = usvisa_data.get_usvisa_input_data_frame()
        model_predictor = USvisaClassifier()
        value = model_predictor.predict(dataframe=usvisa_df)[0]
        status = "Visa Approved" if value == 1 else "Visa Not-Approved"

        return render_template("usvisa.html", context=status)

    except Exception as e:
        return {"status": False, "error": str(e)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)