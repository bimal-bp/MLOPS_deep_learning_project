import sys 
from xray.cloud_storage.s3_ops import S3Operation 

from xray.entity.config_entity import ModelPusherConfig 
from xray.excep.exception import xrayexception 
from xray.logs.logger import logging 

class ModelPusher:
    def __init__(self,model_pusher_config: ModelPusherConfig):
        self.model_pusher_config=model_pusher_config
        self.s3=S3Operation()


    def initiate_model_pusher(self):
        logging.info("Entered model pusher system")

        try:
            self.s3.upload_file(
                "model/model.pt",
                "model.pt",
                "lungxray24",
                remove=False,
            )

            logginf.info("Upload to s3")
        except Exception as e:
            raise e