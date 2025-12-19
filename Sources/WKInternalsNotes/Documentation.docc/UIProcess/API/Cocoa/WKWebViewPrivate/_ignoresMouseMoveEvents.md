# ``WKInternalsNotes/WKWebView/_ignoresMouseMoveEvents``

`_ignoresMouseMoveEvents` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite, setter=_setIgnoresMouseMoveEvents:) BOOL _ignoresMouseMoveEvents WK_API_AVAILABLE(macos(13.0));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setIgnoresMouseMoveEvents:`。

## References
- [`WKWebViewPrivate.h#L827`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L827)
- [`WKWebViewMac.mm#L1477`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1477)
- [`WKWebViewMac.mm#L1477`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1477)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
