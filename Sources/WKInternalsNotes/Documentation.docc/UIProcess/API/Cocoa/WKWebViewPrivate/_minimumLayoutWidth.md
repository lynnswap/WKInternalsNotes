# ``WKInternalsNotes/WKWebView/_minimumLayoutWidth``

`_minimumLayoutWidth` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setMinimumLayoutWidth:) CGFloat _minimumLayoutWidth WK_API_AVAILABLE(macos(10.12));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setMinimumLayoutWidth:`。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L856`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L856)
- [`API/mac/WKWebViewMac.mm#L1741`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1741)
- [`API/mac/WKWebViewMac.mm#L1746`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1746)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
