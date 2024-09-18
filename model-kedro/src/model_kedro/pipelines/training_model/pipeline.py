from kedro.pipeline import Pipeline, node, pipeline
from model_kedro.pipelines.training_model import nodes


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                nodes.generate_model,
                inputs=["train_df"],
                outputs="hub_events",
                name="get_all_events_from_hub",
            ),
        ]
    )
