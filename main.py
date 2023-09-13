import logging
import base64
from datetime import datetime
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction

logger = logging.getLogger(__name__)

class TesteExtension(Extension):

    def __init__(self):
        logger.info('init Teste extension')
        super(TesteExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []

        currentDate = datetime.today().strftime('%Y-%m-%d')
        currentDateBytes = currentDate.encode("ascii")

        base64Bytes = base64.b64encode(currentDateBytes)
        base64String = base64Bytes.decode("ascii")

        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name="Tools Key",
                                         description=base64String,
                                         highlightable=False,
                                         on_enter=CopyToClipboardAction(base64String)
                                         ))

        return RenderResultListAction(items)

if __name__ == '__main__':
    TesteExtension().run()