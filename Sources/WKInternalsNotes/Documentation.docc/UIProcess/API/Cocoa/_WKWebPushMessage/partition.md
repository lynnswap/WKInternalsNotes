# ``WKInternalsNotes/_WKWebPushMessage/partition``

プッシュメッセージのパーティション識別子を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *partition;
```

## Default Value
内部の `WebPushMessage` が保持する値を返す。

## Discussion
`API::WebPushMessage` の `partition()` を `NSString` に変換して返す。

## References
- [`_WKWebPushMessage.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushMessage.h#L38)
- [`_WKWebPushMessage.mm#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushMessage.mm#L56)
- [`_WKWebPushMessage.mm#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushMessage.mm#L58)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
