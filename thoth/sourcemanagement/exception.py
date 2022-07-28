#!/usr/bin/env python3
# Source Management
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

"""Exceptions and errors that can be found in Kebechet."""

from delegator import Command


class SourceManagementExceptionError(Exception):
    """A base class for Kebechet exception hierarchy."""


class ConfigurationError(SourceManagementExceptionError):
    """Raised on error in configuration file."""


class PipenvError(SourceManagementExceptionError):
    """Raised on missing/invalid Pipenv or Pipenv.lock file."""

    def __init__(self, command: Command, *args, **kwargs):
        """Asssign values for exception so that they can be used in issue reports automatically."""
        self.command = command.cmd
        self.stdout = command.out
        self.stderr = command.err
        self.raw_command = command
        super().__init__(*args)


class PullRequestError(SourceManagementExceptionError):
    """Raised in case of failed pull request."""


class CannotFetchPRError(SourceManagementExceptionError):
    """An exception raised if there OGR cannot fetch the PR's for a repo.

    Generally the token is invalid or doesn't have access to the repo.
    """


class CannotFetchBranchesError(SourceManagementExceptionError):
    """An exception raised if there OGR cannot fetch the repo branches.

    Generally the token is invalid or doesn't have access to the repo.
    """


class CreatePRError(SourceManagementExceptionError):
    """An exception raised if there OGR cannot create an PR.

    Generally the token is invalid or doesn't have access to the repo.
    """
