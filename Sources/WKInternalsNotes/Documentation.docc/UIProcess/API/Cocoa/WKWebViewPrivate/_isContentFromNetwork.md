# ``WKInternalsNotes/WKWebView/_isContentFromNetwork``

`_isContentFromNetwork` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _isContentFromNetwork WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivate.h#L178`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L178)
- [`WKWebView.mm#L3841`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3841)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
