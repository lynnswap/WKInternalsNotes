# ``WKInternalsNotes/WKWebView/_networkProcessIdentifier``

`_networkProcessIdentifier` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) pid_t _networkProcessIdentifier;
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivateForTesting.h#L105`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L105)
- [`WKWebViewTesting.mm#L321`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L321)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
