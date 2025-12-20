# ``WKInternalsNotes/_WKWebPushMessage/new()``

直接生成できない。

## Objective-C Declaration
```objective-c
+ (instancetype)new NS_UNAVAILABLE;
```

## Discussion
ヘッダで `NS_UNAVAILABLE` 指定のため `new` は使用できない。`API::WebPushMessage` のラッパーとして内部生成される。

## References
- [`_WKWebPushMessage.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushMessage.h#L33)
- [`_WKWebPushMessageInternal.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushMessageInternal.h#L33)
- [`_WKWebPushMessageInternal.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushMessageInternal.h#L39)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
