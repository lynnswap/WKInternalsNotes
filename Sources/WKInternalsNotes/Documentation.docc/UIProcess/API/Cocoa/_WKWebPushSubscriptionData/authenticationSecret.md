# ``WKInternalsNotes/_WKWebPushSubscriptionData/authenticationSecret``

認証用の shared secret を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSData *authenticationSecret;
```

## Default Value
内部の `WebPushSubscriptionData` が保持する値を返す。

## Discussion
`API::WebPushSubscriptionData::sharedAuthenticationSecret` を `NSData` に変換して返す。

## References
- [`_WKWebPushSubscriptionData.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushSubscriptionData.h#L38)
- [`_WKWebPushSubscriptionData.mm#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushSubscriptionData.mm#L52)
- [`_WKWebPushSubscriptionData.mm#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushSubscriptionData.mm#L54)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
