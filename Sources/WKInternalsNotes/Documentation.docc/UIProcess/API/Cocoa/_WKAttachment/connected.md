# ``WKInternalsNotes/_WKAttachment/connected``

添付がドキュメントに挿入済みかどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isConnected) BOOL connected WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
`Attachment::InsertionState` が `Inserted` の場合に `YES` を返す。

## References
- [`_WKAttachment.h#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.h#L58)
- [`_WKAttachment.mm#L191`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L191)
- [`_WKAttachment.mm#L193`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L193)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
