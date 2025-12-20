# ``WKInternalsNotes/_WKWebPushSubscriptionData/applicationServerKey``

アプリケーションサーバーの公開鍵を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSData *applicationServerKey;
```

## Default Value
内部の `WebPushSubscriptionData` が保持する値を返す。

## Discussion
`API::WebPushSubscriptionData::applicationServerKey` を `NSData` に変換して返す。

## References
- [`_WKWebPushSubscriptionData.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushSubscriptionData.h#L37)
- [`_WKWebPushSubscriptionData.mm#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushSubscriptionData.mm#L47)
- [`_WKWebPushSubscriptionData.mm#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushSubscriptionData.mm#L49)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
