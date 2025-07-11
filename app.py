from flask import Flask, render_template, request
from menstruration_app import UserAccount


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    if request.method == 'POST':
        try:
            user = UserAccount(
                name=request.form['name'],
                age=int(request.form['age']),
                cycle_length=int(request.form['cycle_length']),
                period_length=int(request.form['period_length']),
                last_period_date=request.form['last_period_date']
            )
            return render_template("result.html",
                                   name=user.name,
                                   next_period=user.get_next_period_day().strftime("%Y-%m-%d"),
                                   safe_days=user.get_safe_and_unsafe_days(),
                                   tools=user.show_safe_sex_tools.__doc__)
        except Exception as e:
            return f"Error: {e}"
    return render_template("index_one.html")


if __name__ == '__main__':
    app.run(debug=True)
