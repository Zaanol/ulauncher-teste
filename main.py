import logging
import uuid
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction

logger = logging.getLogger(__name__)


class TesteExtension(Extension):

    def __init__(self):
        logger.info('init UUID extension')
        super(TesteExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []

        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name="Teste novo",
                                         description="Teste 3",
                                         highlightable=False,
                                         on_enter=CopyToClipboardAction("Teste 3")
                                         ))

        return RenderResultListAction(items)


if __name__ == '__main__':
    TesteExtension().run()
