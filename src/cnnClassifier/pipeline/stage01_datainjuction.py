from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.data_injuctions import DataIngestion
from src.cnnClassifier import logger

Stage_name='Data Ingestion stage'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        
        
if __name__=="__main__":
    try:
        logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
        obj= DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {Stage_name} completed <<<<<<")    
    except Exception as e:
        logger.exception(e)