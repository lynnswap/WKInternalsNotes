# ``WKInternalsNotes/WKWebView/_printProvider``

`_printProvider` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) id <_WKWebViewPrintProvider> _printProvider;
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewInternal.h#L648`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewInternal.h#L648)
- [`WKWebViewIOS.mm#L5324`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L5324)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
