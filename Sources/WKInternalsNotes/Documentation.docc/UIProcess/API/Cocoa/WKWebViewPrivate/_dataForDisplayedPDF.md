# ``WKInternalsNotes/WKWebView/_dataForDisplayedPDF``

`_dataForDisplayedPDF` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSData *_dataForDisplayedPDF WK_API_DEPRECATED_WITH_REPLACEMENT("-_getMainResourceDataWithCompletionHandler:", ios(8.0, 26.0), visionos(1.0, 26.0));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivate.h#L716`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L716)
- [`WKWebViewIOS.mm#L4419`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4419)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
