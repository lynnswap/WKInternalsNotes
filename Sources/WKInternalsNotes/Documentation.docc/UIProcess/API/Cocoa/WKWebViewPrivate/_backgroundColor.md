# ``WKInternalsNotes/WKWebView/_backgroundColor``

`_backgroundColor` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setBackgroundColor:) NSColor *_backgroundColor WK_API_AVAILABLE(macos(10.14));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setBackgroundColor:`。

## References
- [`WKWebViewPrivate.h#L839`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L839)
- [`WKWebViewMac.mm#L1527`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1527)
- [`WKWebViewMac.mm#L1527`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1527)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
