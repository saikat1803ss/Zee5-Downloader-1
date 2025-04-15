import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import pyrogram



if __name__ == "__main__" :
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "Zee5",
        bot_token=Config.7909324217:AAHAYG2KoMR47pcOowkd_3jr09U_B2ezgXs,
        api_id=Config.23617515,
        api_hash=Config.9568aa2638f7002e5b7af5971430adad,
        plugins=plugins
    )
    Config.AUTH_USERS.add(680815375)
    app.run()
