# ``WKInternalsNotes/WKWebView/_page()``

`_page` を実行する。

## Objective-C Declaration
```objective-c
- (NakedPtr<WebKit::WebPageProxy>)_page;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewInternal.h#L607`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewInternal.h#L607)
- [`WKWebView.mm#L2160`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L2160)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
