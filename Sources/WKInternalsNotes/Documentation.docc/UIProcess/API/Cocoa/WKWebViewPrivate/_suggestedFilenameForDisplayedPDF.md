# ``WKInternalsNotes/WKWebView/_suggestedFilenameForDisplayedPDF``

`_suggestedFilenameForDisplayedPDF` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *_suggestedFilenameForDisplayedPDF WK_API_DEPRECATED("No longer supported.", ios(8.0, 26.0), visionos(1.0, 26.0));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivate.h#L717`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L717)
- [`WKWebViewIOS.mm#L4424`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4424)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
