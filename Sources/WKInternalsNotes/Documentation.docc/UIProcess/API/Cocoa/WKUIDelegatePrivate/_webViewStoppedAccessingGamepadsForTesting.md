# ``WKInternalsNotes/WKUIDelegatePrivate/_webViewStoppedAccessingGamepadsForTesting(_:)``

ゲームパッドアクセス停止をテスト用に delegate へ通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewStoppedAccessingGamepadsForTesting:(WKWebView *)webView WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
UIDelegate::UIClient がテスト用途の通知として delegate を呼び出す。

## References
- [`WKUIDelegatePrivate.h#L222`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L222)
- [`UIDelegate.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
