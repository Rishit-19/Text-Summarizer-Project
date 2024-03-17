from TextSummarizer.pipeline.Stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.Stage_02_data_validation import DataValidationTrainingPipeline
from TextSummarizer.pipeline.Stage_03_data_transformation import DataTransformationTrainingPipeline
from TextSummarizer.pipeline.Stage_04_model_trainer import ModelTrainerTrainingPipeline
from TextSummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f"-----stage{STAGE_NAME} started-----")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"-----stage {STAGE_NAME} completed-----\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation stage"
try:
    logger.info(f"-----stage{STAGE_NAME} started-----")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"-----stage {STAGE_NAME} completed-----\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f"-----stage{STAGE_NAME} started-----")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"-----stage {STAGE_NAME} completed-----\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f"-----stage{STAGE_NAME} started-----")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f"-----stage {STAGE_NAME} completed-----\n\n")
except Exception as e:
    logger.exception(e)
    raise e