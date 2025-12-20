# ``WKInternalsNotes/_WKWebPushSubscriptionData/ecdhPublicKey``

クライアントの ECDH 公開鍵を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSData *ecdhPublicKey;
```

## Default Value
内部の `WebPushSubscriptionData` が保持する値を返す。

## Discussion
`API::WebPushSubscriptionData::clientECDHPublicKey` を `NSData` に変換して返す。

## References
- [`_WKWebPushSubscriptionData.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushSubscriptionData.h#L39)
- [`_WKWebPushSubscriptionData.mm#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushSubscriptionData.mm#L57)
- [`_WKWebPushSubscriptionData.mm#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushSubscriptionData.mm#L59)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
