# ``WKInternalsNotes/_WKWebPushMessage/scopeURL``

プッシュメッセージの scope URL を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSURL *scopeURL;
```

## Default Value
内部の `WebPushMessage` が保持する scope から生成される。

## Discussion
`API::WebPushMessage` の `scope()` を `NSURL` に変換して返す。

## References
- [`_WKWebPushMessage.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushMessage.h#L36)
- [`_WKWebPushMessage.mm#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushMessage.mm#L51)
- [`_WKWebPushMessage.mm#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushMessage.mm#L53)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
