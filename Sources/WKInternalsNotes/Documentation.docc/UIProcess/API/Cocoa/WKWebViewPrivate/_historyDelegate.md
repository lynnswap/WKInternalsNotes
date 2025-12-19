# ``WKInternalsNotes/WKWebView/_historyDelegate``

`_historyDelegate` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak, setter=_setHistoryDelegate:) id <WKHistoryDelegatePrivate> _historyDelegate;
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setHistoryDelegate:`。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L185`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L185)
- [`API/Cocoa/WKWebView.mm#L4210`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4210)
- [`API/Cocoa/WKWebView.mm#L4215`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4215)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
