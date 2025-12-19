# ``WKInternalsNotes/WKWebView/_protectedPage()``

`_protectedPage` を実行する。

## Objective-C Declaration
```objective-c
- (RefPtr<WebKit::WebPageProxy>)_protectedPage;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewInternal.h#L608`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewInternal.h#L608)
- [`WKWebView.mm#L2165`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L2165)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
