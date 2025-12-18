# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:adjustedDataInteractionItemProvidersForItemProvider:representingObjects:additionalData:)``

ドラッグ用 item provider を delegate で調整する。

## Objective-C Declaration
```objective-c
- (NSArray *)_webView:(WKWebView *)webView adjustedDataInteractionItemProvidersForItemProvider:(id)itemProvider representingObjects:(NSArray *)representingObjects additionalData:(NSDictionary *)additionalData WK_API_AVAILABLE(ios(11.0));
```

## Discussion
WKContentViewInteraction が `NSItemProvider` と対応する `representingObjects` / `additionalData` をまとめ、delegate が返した配列を drag items に追加する。

## References
- [`WKUIDelegatePrivate.h#L275`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L275)
- [`WKContentViewInteraction.mm#L11009`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L11009)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
