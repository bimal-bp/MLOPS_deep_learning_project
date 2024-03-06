import sys

from xray.excep.exception import xrayexception
from xray.pipeline.train_pipeline import TrainPipeline


def start_training():
    try:
        train_pipeline = TrainPipeline()

        train_pipeline.run_pipeline()

    except Exception as e:
        raise xrayexception(e, sys)


if __name__ == "__main__":
    start_training()