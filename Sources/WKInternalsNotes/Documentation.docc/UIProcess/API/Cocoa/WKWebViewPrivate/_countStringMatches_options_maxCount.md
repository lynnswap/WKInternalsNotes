# ``WKInternalsNotes/WKWebView/_countStringMatches(_:options:maxCount:)``

`_countStringMatches` を実行する。

## Objective-C Declaration
```objective-c
- (void)_countStringMatches:(NSString *)string options:(_WKFindOptions)options maxCount:(NSUInteger)maxCount;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L390`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L390)
- [`WKWebView.mm#L5694`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5694)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
