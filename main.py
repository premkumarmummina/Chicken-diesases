from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage01_datainjuction import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage02_preparebasemodel import preparebasemodeltrainingpipeline
from src.cnnClassifier.pipeline.stage03_training_and_recall import training_and_Recall
from src.cnnClassifier.pipeline.stage04_evalution import EvaluationPipeline

Stage_name='Data Ingestion stage'

if __name__=="__main__":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
        obj= DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {Stage_name} completed <<<<<<")    
    except Exception as e:
        logger.exception(e)
        
Stage_name='Prepare Base Model'       
        
if __name__=="__main__":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
        obj= preparebasemodeltrainingpipeline()
        obj.main()
        logger.info(f">>>>>> stage {Stage_name} completed <<<<<<")    
    except Exception as e:
        logger.exception(e)
        

Stage_name='Training and Recall'
       
if __name__=="__main__":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
        obj= training_and_Recall()
        obj.main()
        logger.info(f">>>>>> stage {Stage_name} completed <<<<<<")    
    except Exception as e:
        logger.exception(e)
        
STAGE_NAME='Evalution'     

if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    