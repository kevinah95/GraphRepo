# Copyright 2020 NullConvergence
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
"""This module is a custom miner class with some abstractions"""
from abc import abstractmethod


class DefaultMapper:
    """The miners are currently synchronous, but
    ideally they will be async in the future"""

    def __init__(self):
        pass

    @abstractmethod
    def map(self, objects):
        """Maps objects"""
        raise NotImplementedError
