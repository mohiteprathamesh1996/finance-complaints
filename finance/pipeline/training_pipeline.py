from finance.entity.config_entity import (
    TrainingPipelineConfig,
    DataIngestionConfig
)


from finance.exception import FinanceException
from finance.logger import logging

from finance.entity.artifact_entity import (
    DataIngestionArtifact
)

from finance.component.data_ingestion import DataIngestion


import sys


class TrainPipeline:
    def __init__(self):
        training_pipeline_config = TrainingPipelineConfig()
        self.training_pipeline_config = training_pipeline_config

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            self.data_ingestion_config = DataIngestionConfig(
                training_pipeline_config=self.training_pipeline_config
            )
            logging.info("Starting data ingestion")
            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config
                )
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(
                f"Data ingestion completed and artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact

        except Exception as e:
            raise FinanceException(e, sys)

    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise FinanceException(e, sys)
