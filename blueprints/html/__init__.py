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
from flask import abort
from flask import Blueprint
from flask import render_template
from flask import send_from_directory

html_module = Blueprint("html_module", __name__, template_folder="templates")


@html_module.route("/misc/full-url.html")
def full_url():
  return render_template("full-url.html")


@html_module.route("/misc/path-relative-url.html")
def path_relative_url():
  return render_template("path-relative-url.html")


@html_module.route("/misc/protocol-relative-url.html")
def protocol_relative_url():
  return render_template("protocol-relative-url.html")


@html_module.route("/<path:path>")
def html_dir(path):
  return send_from_directory("test-cases/html", path)
