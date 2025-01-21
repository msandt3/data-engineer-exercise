import dlt
from dlt.sources.rest_api import (
    RESTAPIConfig,
    rest_api_resources,
)


@dlt.source
def spacex_source():
    config: RESTAPIConfig = {
        "client": {
            "base_url": "https://api.spacexdata.com/v4/",
        },
        # The default configuration for all resources and their endpoints
        "resource_defaults": {
            "primary_key": "id",
            "write_disposition": "merge"
        },
        "resources": [
            {
                "name": "launches",
                "endpoint": {
                    "path": "launches"
                }
            }
        ],
    }

    yield from rest_api_resources(config)


def load_spacex() -> None:
    pipeline = dlt.pipeline(
        pipeline_name="rest_api_spacex",
        destination=dlt.destinations.duckdb("data.duckdb"),
        dataset_name="space_x_data",
        progress="log",
    )
    
    load_info = pipeline.run(spacex_source())
    print(load_info)  # noqa: T201

if __name__ == "__main__":
    load_spacex()