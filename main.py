from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage01_datainjuction import DataIngestionTrainingPipeline

Stage_name='Data Ingestion stage'

if __name__=="__main__":
    try:
        logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
        obj= DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {Stage_name} completed <<<<<<")    
    except Exception as e:
        logger.exception(e)