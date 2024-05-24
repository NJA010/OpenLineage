# Copyright 2018-2024 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations
from attr import define
from openlineage.client import utils
from openlineage.client.generated.base import JobFacet


@define
class DocumentationJobFacet(JobFacet):
    description: str
    """The description of the job."""

    @staticmethod
    def _get_schema() -> str:
        return (
            "https://openlineage.io/spec/facets/1-0-1/DocumentationJobFacet.json#/$defs/DocumentationJobFacet"
        )


utils.register_facet_key("documentation", DocumentationJobFacet)
