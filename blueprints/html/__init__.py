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
"""Module serving all the traffic for html test cases."""
import os
from flask import abort
from flask import Blueprint
from flask import render_template
from flask import Response
from flask import send_from_directory

html_module = Blueprint("html_module", __name__, template_folder="templates")

# Global app.instance_path is not accessible from blueprints ¯\_(ツ)_/¯.
TEST_CASES_PATH = os.path.abspath(__file__ + "/../../../test-cases/html/")


@html_module.route("/misc/url/full-url/")
def full_url():
  return render_template("url/full-url.html")


@html_module.route("/misc/url/path-relative-url/")
def path_relative_url():
  return render_template("url/path-relative-url.html")


@html_module.route("/misc/url/protocol-relative-url/")
def protocol_relative_url():
  return render_template("url/protocol-relative-url.html")


@html_module.route("/misc/string/url-string/")
def inline_url_string():
  return render_template("string/url-string.html")


@html_module.route("/", defaults={"path": ""})
@html_module.route("/<path:path>")
def html_dir(path):
  """Lists contents of requested directory."""
  requested_path = os.path.join(TEST_CASES_PATH, path)
  if not os.path.exists(requested_path):
    return abort(404)

  if os.path.isdir(requested_path):
    files = os.listdir(requested_path)
    return render_template("list-html-dir.html", files=files, path=path)

  if os.path.isfile(requested_path):
    return send_from_directory("test-cases/html", path)
