# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:willPerformDropWithSession:)``

ドロップ実行前にドラッグアイテムを delegate に取得させる。

## Objective-C Declaration
```objective-c
- (NSArray<UIDragItem *> *)_webView:(WKWebView *)webView willPerformDropWithSession:(id <UIDropSession>)session WK_API_AVAILABLE(ios(11.0));
```

## Discussion
WKContentViewInteraction が delegate から返った `UIDragItem` を item providers に変換し、空ならドロップ処理を中断する。

## References
- [`WKUIDelegatePrivate.h#L287`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L287)
- [`WKContentViewInteraction.mm#L11428`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L11428)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
