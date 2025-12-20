# ``WKInternalsNotes/_WKWebPushSubscriptionData/init()``

直接初期化できない。

## Objective-C Declaration
```objective-c
- (instancetype)init NS_UNAVAILABLE;
```

## Discussion
ヘッダで `NS_UNAVAILABLE` 指定のため `init` は使用できない。`API::WebPushSubscriptionData` のラッパーとして内部生成される。

## References
- [`_WKWebPushSubscriptionData.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushSubscriptionData.h#L34)
- [`_WKWebPushSubscriptionDataInternal.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushSubscriptionDataInternal.h#L33)
- [`_WKWebPushSubscriptionDataInternal.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushSubscriptionDataInternal.h#L39)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
