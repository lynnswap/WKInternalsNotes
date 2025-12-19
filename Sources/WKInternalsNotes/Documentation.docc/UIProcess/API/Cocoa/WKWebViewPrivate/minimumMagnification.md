# ``WKInternalsNotes/WKWebView/minimumMagnification``

`minimumMagnification` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) CGFloat minimumMagnification WK_API_AVAILABLE(macos(15.0));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivate.h#L874`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L874)
- [`WKWebViewMac.mm#L1916`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1916)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
