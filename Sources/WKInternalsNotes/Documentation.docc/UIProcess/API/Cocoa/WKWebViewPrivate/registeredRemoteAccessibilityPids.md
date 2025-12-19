# ``WKInternalsNotes/WKWebView/registeredRemoteAccessibilityPids()``

`registeredRemoteAccessibilityPids` を実行する。

## Objective-C Declaration
```objective-c
- (NSArray<NSNumber *> *)registeredRemoteAccessibilityPids;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L645`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L645)
- [`WKWebView.mm#L6528`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6528)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
