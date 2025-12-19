# ``WKInternalsNotes/WKWebView/_textManipulationDelegate``

`_textManipulationDelegate` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak, setter=_setTextManipulationDelegate:) id <_WKTextManipulationDelegate> _textManipulationDelegate WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setTextManipulationDelegate:`。

## References
- [`WKWebViewPrivate.h#L259`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L259)
- [`WKWebView.mm#L3912`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3912)
- [`WKWebView.mm#L3912`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3912)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
