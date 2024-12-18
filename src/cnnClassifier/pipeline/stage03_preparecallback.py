from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.prepare_callbacks import PrepareCallback
from  src.cnnClassifier import logger

Stage_name='Prepare recall backs'

class preparerecallbackstrainingpipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()
                
        
if __name__=="__main__":
    try:
        logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
        obj= preparerecallbackstrainingpipeline()
        obj.main()
        logger.info(f">>>>>> stage {Stage_name} completed <<<<<<")    
    except Exception as e:
        logger.exception(e)