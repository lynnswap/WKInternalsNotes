# ``WKInternalsNotes/WKWebView/_showWarningView(_:completionHandler:)``

`_showWarningView` を表示する。

## Objective-C Declaration
```objective-c
- (void)_showWarningView:(const WebKit::BrowsingWarning&)warning completionHandler:(CompletionHandler<void(Variant<WebKit::ContinueUnsafeLoad, URL>&&)>&&)completionHandler;
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewInternal.h#L557`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewInternal.h#L557)
- [`WKWebView.mm#L1909`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L1909)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
