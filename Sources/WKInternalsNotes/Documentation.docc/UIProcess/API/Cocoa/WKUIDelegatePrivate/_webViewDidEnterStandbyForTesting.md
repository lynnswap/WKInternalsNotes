# ``WKInternalsNotes/WKUIDelegatePrivate/_webViewDidEnterStandbyForTesting(_:)``

テスト用スタンバイ開始を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewDidEnterStandbyForTesting:(WKWebView *)webView WK_API_AVAILABLE(ios(26.0));
```

## Discussion
UIDelegate::UIClient の `didEnterStandby` でテスト用途として通知される。

## References
- [`WKUIDelegatePrivate.h#L306`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L306)
- [`UIDelegate.mm#L2291`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L2291)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
