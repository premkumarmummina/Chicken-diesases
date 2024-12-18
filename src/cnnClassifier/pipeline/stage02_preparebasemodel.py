from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.prepare_basemodel import PrepareBaseModel
from  src.cnnClassifier import logger

Stage_name='Prepare Base Model'

class preparebasemodeltrainingpipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
            
        
if __name__=="__main__":
    try:
        logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
        obj= preparebasemodeltrainingpipeline()
        obj.main()
        logger.info(f">>>>>> stage {Stage_name} completed <<<<<<")    
    except Exception as e:
        logger.exception(e)