from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

TEMPLATE = """
<h2>Starcloud Maintenance Console</h2>
<form method="POST">
  <label>Username:</label><br>
  <input name="username" /><br>
  <label>Password:</label><br>
  <input name="password" type="password" /><br><br>
  <input type="submit" value="Login" />
</form>
{% if error %}
<p style="color:red">{{ error }}</p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("username")
        pw = request.form.get("password")
        if user == "admin" and pw == "spacewalk":
            return redirect("/admin")
        elif user == "" or pw == "":
            return render_template_string(TEMPLATE, error="Missing credentials.")
        else:
            return render_template_string(TEMPLATE, error="Access Denied.")
    return render_template_string(TEMPLATE, error=None)

@app.route("/admin")
def admin():
    return "<h3>Admin Panel</h3><p>Flag: flag{ghost_login_successful}</p>"
