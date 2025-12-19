# ``WKInternalsNotes/WKWebView/_completeTextManipulation(_:completion:)``

`_completeTextManipulation` を実行する。

## Objective-C Declaration
```objective-c
- (void)_completeTextManipulation:(_WKTextManipulationItem *)item completion:(void(^)(BOOL success))completionHandler WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Discussion
`completion` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L261`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L261)
- [`API/Cocoa/WKWebView.mm#L4044`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4044)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
