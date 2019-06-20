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
"""Module serving all the traffic for css test cases."""
import os
from flask import abort
from flask import Blueprint
from flask import make_response
from flask import render_template
from flask import Response
from flask import send_from_directory
from flask import url_for

css_module = Blueprint("css_module", __name__, template_folder="templates")

# Global app.instance_path is not accessible from blueprints ¯\_(ツ)_/¯.
TEST_CASES_PATH = os.path.abspath(__file__ + "/../../../test-cases/css/")


@css_module.route("/font-face.css")
def css():
  content = "@font-face{font-family: leak;src: url(" + url_for(
      "index", _external=True) + "test/css/font-face.found);}"
  r = make_response(content, 200)
  r.headers["Content-Type"] = "text/css"
  return r


@css_module.route("/", defaults={"path": ""})
@css_module.route("/<path:path>")
def html_dir(path):
  """Lists contents of requested directory."""
  requested_path = os.path.join(TEST_CASES_PATH, path)
  if not os.path.exists(requested_path):
    return abort(404)

  if os.path.isdir(requested_path):
    files = os.listdir(requested_path)
    return render_template("list-css-dir.html", files=files, path=path)

  if os.path.isfile(requested_path):
    return send_from_directory("test-cases/css", path)
