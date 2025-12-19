# ``WKInternalsNotes/WKWebView/_fixedLayoutSize``

`_fixedLayoutSize` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setFixedLayoutSize:) CGSize _fixedLayoutSize;
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setFixedLayoutSize:`。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L288`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L288)
- [`API/Cocoa/WKWebView.mm#L5946`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5946)
- [`API/Cocoa/WKWebView.mm#L5951`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5951)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
