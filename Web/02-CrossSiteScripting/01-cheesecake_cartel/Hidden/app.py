from flask import Flask, render_template, request, redirect
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from time import sleep
import threading

run_browser_headless = True

admin_session = "YWxtb3N0IHRoZXJlIQ=="
initial_comment = {
  "content": "<b>Hello internet!</b>",
  "author": "stackotter's grandma"
}
comments = [initial_comment]

chrome_options = webdriver.ChromeOptions()
if run_browser_headless:
  chrome_options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

def setup_driver():
  print("Loading webdriver")
  sleep(1)
  driver.get("http://localhost:8083/")
  driver.add_cookie({"name": "SESSION", "value": admin_session})
  print("Finished loading webdriver")

def visit_recipe_as_admin():
  try:
    driver.get("http://localhost:8083/")
  except:
    driver.refresh()
  return

def comment_cleanup_loop():
  global comments
  while True:
    sleep(60 * 5)
    comments = [initial_comment]

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html", comments=comments)

@app.route("/admin")
def admin():
  if not "SESSION" in request.cookies or request.cookies["SESSION"] != admin_session:
    return "Not authorized", 403
  return render_template("admin.html")

@app.route("/add-comment", methods=["POST"])
def add_comment():
  if not "content" in request.form or not "author" in request.form:
    return "Bad request", 400

  comments.append({
    "content": request.form["content"],
    "author": request.form["author"]
  })

  visit_recipe_as_admin()
  return redirect("/")

def run_app():
  app.run("0.0.0.0", port=8083)

driver_thread = threading.Thread(target=setup_driver)
driver_thread.start()
run_app()
