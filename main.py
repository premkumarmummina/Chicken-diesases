from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage01_datainjuction import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stge02_preparebasemodel import preparebasemodeltrainingpipeline
from src.cnnClassifier.pipeline.stage03_preparecallback import preparerecallbackstrainingpipeline

Stage_name='Data Ingestion stage'

if __name__=="__main__":
    try:
        logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
        obj= DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {Stage_name} completed <<<<<<")    
    except Exception as e:
        logger.exception(e)
        
Stage_name='Prepare Base Model'       
        
if __name__=="__main__":
    try:
        logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
        obj= preparebasemodeltrainingpipeline()
        obj.main()
        logger.info(f">>>>>> stage {Stage_name} completed <<<<<<")    
    except Exception as e:
        logger.exception(e)
        

Stage_name='Prepare recall backs'
       
if __name__=="__main__":
    try:
        logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
        obj= preparerecallbackstrainingpipeline()
        obj.main()
        logger.info(f">>>>>> stage {Stage_name} completed <<<<<<")    
    except Exception as e:
        logger.exception(e)
    