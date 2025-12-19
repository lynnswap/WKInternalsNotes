# ``WKInternalsNotes/WKWebView/_lastNavigationWasAppInitiated(_:)``

`_lastNavigationWasAppInitiated` を実行する。

## Objective-C Declaration
```objective-c
- (void)_lastNavigationWasAppInitiated:(void(^)(BOOL))completionHandler;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivateForTesting.h#L136`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L136)
- [`API/Cocoa/WKWebViewTesting.mm#L665`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L665)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
