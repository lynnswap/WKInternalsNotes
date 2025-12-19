# ``WKInternalsNotes/WKWebView/_iconLoadingDelegate``

`_iconLoadingDelegate` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak, setter=_setIconLoadingDelegate:) id <_WKIconLoadingDelegate> _iconLoadingDelegate;
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setIconLoadingDelegate:`。

## References
- [`WKWebViewPrivate.h#L186`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L186)
- [`WKWebView.mm#L696`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L696)
- [`WKWebView.mm#L696`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L696)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
