# ``WKInternalsNotes/WKWebView/_editable``

`_editable` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, getter=_isEditable, setter=_setEditable:) BOOL _editable WK_API_AVAILABLE(macos(10.11), ios(9.0));
```

## Discussion
getter/setter を通じて値を取得/設定する。 getter は `_isEditable`。 setter は `_setEditable:`。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L229`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L229)
- [`API/Cocoa/WKWebView.mm#L3880`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3880)
- [`API/Cocoa/WKWebView.mm#L3885`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3885)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
