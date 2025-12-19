# ``WKInternalsNotes/WKWebView/_minimumLayoutWidth``

`_minimumLayoutWidth` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setMinimumLayoutWidth:) CGFloat _minimumLayoutWidth WK_API_AVAILABLE(macos(10.12));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setMinimumLayoutWidth:`。

## References
- [`WKWebViewPrivate.h#L852`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L852)
- [`WKWebViewMac.mm#L1741`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1741)
- [`WKWebViewMac.mm#L1741`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1741)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
