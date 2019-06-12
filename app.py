# Copyright 2019 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""The entry point for Flask App serving the testbed"s content."""
import os
from blueprints.headers import headers_module
from blueprints.html import html_module
from blueprints.javascript import javascript_module
from blueprints.utils import utils_module
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.register_blueprint(headers_module, url_prefix="/headers")
app.register_blueprint(html_module, url_prefix="/html")
app.register_blueprint(javascript_module, url_prefix="/javascript")
app.register_blueprint(utils_module)


@app.route("/")
def index():
  return render_template("index.html")


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
