# ``WKInternalsNotes/WKWebView/_startTextManipulationsWithConfiguration(_:completion:)``

`_startTextManipulationsWithConfiguration` を開始する。

## Objective-C Declaration
```objective-c
- (void)_startTextManipulationsWithConfiguration:(_WKTextManipulationConfiguration *)configuration completion:(void(^)(void))completionHandler WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Discussion
`completion` に結果を返す。

## References
- [`WKWebViewPrivate.h#L260`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L260)
- [`WKWebView.mm#L3939`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3939)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
