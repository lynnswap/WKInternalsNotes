# ``WKInternalsNotes/WKWebView/_inputDelegate``

`_inputDelegate` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak, setter=_setInputDelegate:) id <_WKInputDelegate> _inputDelegate WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setInputDelegate:`。

## References
- [`WKWebViewPrivate.h#L393`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L393)
- [`WKWebView.mm#L5792`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5792)
- [`WKWebView.mm#L5792`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5792)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
