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
"""Module serving all the traffic for javascript test cases."""
from flask import Blueprint
from flask import send_from_directory

javascript_module = Blueprint("javascript_module", __name__)


@javascript_module.route("/<path:path>")
def javascript_dir(path):
  return send_from_directory("test-cases/javascript", path)
