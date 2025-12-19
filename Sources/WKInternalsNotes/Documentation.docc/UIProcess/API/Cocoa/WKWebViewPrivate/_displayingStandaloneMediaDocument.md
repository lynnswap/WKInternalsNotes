# ``WKInternalsNotes/WKWebView/_displayingStandaloneMediaDocument``

`_displayingStandaloneMediaDocument` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=_isDisplayingStandaloneMediaDocument) BOOL _displayingStandaloneMediaDocument;
```

## Discussion
読み取り専用のため setter は持たない。 getter は `_isDisplayingStandaloneMediaDocument`。

## References
- [`WKWebViewPrivate.h#L397`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L397)
- [`WKWebView.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
