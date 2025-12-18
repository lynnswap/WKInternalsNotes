# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:contextMenuDidEndForElement:)``

コンテキストメニュー終了を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView contextMenuDidEndForElement:(WKContextMenuElementInfo *)elementInfo WK_API_AVAILABLE(ios(13.0));
```

## Discussion
コンテキストメニューの終了時に `contextMenuDidEndForElement:` が呼ばれ、UIKit の多重呼び出しを避けるため `_contextMenuElementInfo` がある場合のみ通知する。

## References
- [`WKUIDelegatePrivate.h#L255`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L255)
- [`WKContentViewInteraction.mm#L15440`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L15440)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
