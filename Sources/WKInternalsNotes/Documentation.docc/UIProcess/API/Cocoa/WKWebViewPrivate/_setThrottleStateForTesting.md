# ``WKInternalsNotes/WKWebView/_setThrottleStateForTesting(_:)``

`_setThrottleStateForTesting` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setThrottleStateForTesting:(int)type;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivateForTesting.h#L114`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L114)
- [`API/Cocoa/WKWebViewTesting.mm#L411`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L411)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
