# ``WKInternalsNotes/_WKWebPushSubscriptionData/endpoint``

サブスクリプションの endpoint URL を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSURL *endpoint;
```

## Default Value
内部の `WebPushSubscriptionData` が保持する値を返す。

## Discussion
`API::WebPushSubscriptionData::endpoint` を `NSURL` に変換して返す。

## References
- [`_WKWebPushSubscriptionData.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushSubscriptionData.h#L36)
- [`_WKWebPushSubscriptionData.mm#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushSubscriptionData.mm#L42)
- [`_WKWebPushSubscriptionData.mm#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushSubscriptionData.mm#L44)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
