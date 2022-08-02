from flask import Flask, render_template, request, redirect
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from sys import platform
from time import sleep
import threading
import os

# Load SSL config if any
is_https = False
certfile = os.getenv("CTF_CERTFILE", None)
keyfile = os.getenv("CTF_KEYFILE", None)
ssl_context = None
if not keyfile == None and not certfile == None:
  is_https = True
  ssl_context = (certfile, keyfile)

# Global constants
run_browser_headless = True
admin_session = "YWxtb3N0IHRoZXJlIQ=="
initial_comment = {
  "content": "<b>Hello internet!</b>",
  "author": "stackotter's grandma"
}
port = 8083
domain = os.getenv("CTF_DOMAIN", "localhost")
base_url = "%s://%s:%d/" % ("https" if is_https else "http", domain, port)

# Global state
comments = [initial_comment]

# Load webdriver for comment reading bot
chrome_options = webdriver.ChromeOptions()
if run_browser_headless:
  chrome_options.add_argument("--headless")
if platform == "linux":
  chrome_options.add_argument("--no-sandbox")
  chrome_options.add_argument("--disable-dev-shm-usage")
driver = None
try:
  driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
except Exception as e:
  print(e)
  print("Failed to load Google Chrome browser for the comment reading bot to use. Please install Google Chrome and try again")
  exit(1)

def setup_driver():
  print("Loading webdriver")
  sleep(1)
  driver.get(base_url)
  print(base_url)
  driver.add_cookie({"name": "SESSION", "value": admin_session})
  print("Finished loading webdriver")

def visit_recipe_as_admin():
  try:
    driver.get(base_url)
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
  app.run("0.0.0.0", port=port, ssl_context=ssl_context)

driver_thread = threading.Thread(target=setup_driver)
driver_thread.start()
run_app()
