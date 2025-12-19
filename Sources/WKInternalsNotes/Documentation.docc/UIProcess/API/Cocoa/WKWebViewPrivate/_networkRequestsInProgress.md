# ``WKInternalsNotes/WKWebView/_networkRequestsInProgress``

`_networkRequestsInProgress` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _networkRequestsInProgress;
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivate.h#L268`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L268)
- [`WKWebView.mm#L5291`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5291)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
