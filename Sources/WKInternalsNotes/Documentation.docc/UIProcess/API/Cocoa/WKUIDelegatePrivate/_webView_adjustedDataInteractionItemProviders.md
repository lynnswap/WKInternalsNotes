# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:adjustedDataInteractionItemProviders:)``

Data interaction の item providers を調整するための delegate フック（UIProcess 内の呼び出しは見当たらない）。

## Objective-C Declaration
```objective-c
- (NSArray *)_webView:(WKWebView *)webView adjustedDataInteractionItemProviders:(NSArray *)originalItemProviders WK_API_AVAILABLE(ios(11.0));
```

## Discussion
UIProcess 配下の `.m/.mm` では呼び出しが見当たらず、宣言のみ確認できる。

## References
- [`WKUIDelegatePrivate.h#L253`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L253)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
