# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:performDataInteractionOperationWithItemProviders:)``

ドロップ操作のデータインタラクションを delegate に処理させる。

## Objective-C Declaration
```objective-c
- (BOOL)_webView:(WKWebView *)webView performDataInteractionOperationWithItemProviders:(NSArray *)itemProviders WK_API_AVAILABLE(ios(11.0));
```

## Discussion
dropInteraction の `performDrop:` で delegate が `YES` を返した場合、WebKit の既定処理を実行せずに終了する。

## References
- [`WKUIDelegatePrivate.h#L277`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L277)
- [`WKContentViewInteraction.mm#L11423`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L11423)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
