# ``WKInternalsNotes/WKWebView/_stringForFind``

`_stringForFind` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (class, nonatomic, copy, setter=_setStringForFind:) NSString *_stringForFind WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setStringForFind:`。

## References
- [`WKWebViewPrivate.h#L348`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L348)
- [`WKWebView.mm#L4176`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4176)
- [`WKWebView.mm#L4176`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4176)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
