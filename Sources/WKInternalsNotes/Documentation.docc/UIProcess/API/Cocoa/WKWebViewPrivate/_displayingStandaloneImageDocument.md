# ``WKInternalsNotes/WKWebView/_displayingStandaloneImageDocument``

`_displayingStandaloneImageDocument` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=_isDisplayingStandaloneImageDocument) BOOL _displayingStandaloneImageDocument;
```

## Discussion
読み取り専用のため setter は持たない。 getter は `_isDisplayingStandaloneImageDocument`。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L396`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L396)
- [`API/Cocoa/WKWebView.mm#L5877`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5877)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
