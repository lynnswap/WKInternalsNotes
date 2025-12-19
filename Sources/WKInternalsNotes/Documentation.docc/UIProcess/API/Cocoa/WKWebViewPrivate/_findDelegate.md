# ``WKInternalsNotes/WKWebView/_findDelegate``

`_findDelegate` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak, setter=_setFindDelegate:) id <_WKFindDelegate> _findDelegate;
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setFindDelegate:`。

## References
- [`WKWebViewPrivate.h#L388`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L388)
- [`WKWebView.mm#L5656`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5656)
- [`WKWebView.mm#L5656`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5656)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
