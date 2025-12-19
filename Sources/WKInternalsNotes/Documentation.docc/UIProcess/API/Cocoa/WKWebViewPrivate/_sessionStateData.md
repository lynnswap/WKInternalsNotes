# ``WKInternalsNotes/WKWebView/_sessionStateData``

`_sessionStateData` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSData *_sessionStateData;
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivate.h#L245`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L245)
- [`WKWebView.mm#L4966`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4966)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
