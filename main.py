import logging
import my_module

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


logger.info('Hello logger')


my_module.method_1()
