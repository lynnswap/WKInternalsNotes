# ``WKInternalsNotes/WKUIDelegatePrivate/_webViewDidExitStandbyForTesting(_:)``

テスト用スタンバイ終了を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewDidExitStandbyForTesting:(WKWebView *)webView WK_API_AVAILABLE(ios(26.0));
```

## Discussion
UIDelegate::UIClient の `didExitStandby` でテスト用途として通知される。

## References
- [`WKUIDelegatePrivate.h#L307`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L307)
- [`UIDelegate.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
