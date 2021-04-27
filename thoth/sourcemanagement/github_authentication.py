#!/usr/bin/env python3
# Kebechet
# Copyright(C) 2020 Sai Sankar Gochhayat
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Handle Github APP Authentication."""

from cryptography.hazmat.backends import default_backend
import jwt
import requests
import time
import json
import os
from pathlib import Path

_BASE_URL = "https://api.github.com/"


class GithubAuthentication:
    """Handles getting the OAuth Token for the Github Application."""

    def __init__(self, slug: str) -> None:
        """Initialize and check values."""
        self.slug = slug

        self.github_private_key_path = str(os.getenv("GITHUB_PRIVATE_KEY_PATH"))
        self._file_path = Path(self.github_private_key_path)
        self.github_private_key = None
        with open(self._file_path, "r") as f:
            self.github_private_key = f.read()
        self.github_app_id = os.getenv("GITHUB_APP_ID", None)

        if not self.github_app_id or not self.github_private_key:
            raise ValueError(
                "Cannot authenticate as Github because of missing values. \
                    Please check if APP ID and Private key are set."
            )
        # Read and encode
        self.cert_str = self.github_private_key
        self.cert_bytes = self.cert_str.encode()

    def _get_header(self):
        """Get the application headers for authentication."""
        time_since_epoch_in_seconds = int(time.time())
        private_key = default_backend().load_pem_private_key(self.cert_bytes, None)
        payload = {
            # issued at time
            "iat": time_since_epoch_in_seconds,
            # JWT expiration time (10 minute maximum)
            "exp": time_since_epoch_in_seconds + (10 * 60),
            # GitHub App's identifier
            "iss": str(self.github_app_id),
        }
        jwt_generated = jwt.encode(payload, private_key, algorithm="RS256")

        headers = {
            "Authorization": "Bearer {}".format(jwt_generated),
            "Accept": "application/vnd.github.machine-man-preview+json",
        }
        return headers

    def get_access_token(self) -> str:
        """Fetch the installation ID and use it get the access token."""
        # Logic to fetch installation id of a repo
        # https://docs.github.com/en/free-pro-team@latest/rest/reference/apps#get-a-repository-installation-for-the-authenticated-app
        response = requests.get("{}repos/{}/installation".format(_BASE_URL, self.slug), headers=self._get_header())
        installation_id = json.loads(response.content.decode()).get("id")

        # This is the request to fetch the oauth token.
        response = requests.post(
            "{}app/installations/{}/access_tokens".format(_BASE_URL, installation_id), headers=self._get_header()
        )
        if response.status_code != 201:
            raise ValueError(f"Access token couldn't be fetched. Error - {response.content.decode()}")
        response_dict: dict = json.loads(response.content.decode())
        return response_dict.get("token")  # type: ignore
