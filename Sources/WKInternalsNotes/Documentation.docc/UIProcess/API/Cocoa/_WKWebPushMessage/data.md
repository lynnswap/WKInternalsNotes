# ``WKInternalsNotes/_WKWebPushMessage/data``

プッシュメッセージの payload データを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSData *data;
```

## Default Value
データが存在しない場合は `nil` を返す。

## Discussion
`API::WebPushMessage` の `data()` を `NSData` に変換して返す。

## References
- [`_WKWebPushMessage.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushMessage.h#L37)
- [`_WKWebPushMessage.mm#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushMessage.mm#L43)
- [`_WKWebPushMessage.mm#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushMessage.mm#L45)
- [`_WKWebPushMessage.mm#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushMessage.mm#L46)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
