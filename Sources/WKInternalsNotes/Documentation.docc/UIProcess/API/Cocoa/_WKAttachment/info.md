# ``WKInternalsNotes/_WKAttachment/info``

添付の情報を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, nullable) _WKAttachmentInfo *info WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Default Value
添付が無効な場合は `nil` を返す。

## Discussion
内部の `Attachment` が有効であれば `_WKAttachmentInfo` を生成して返す。

## References
- [`_WKAttachment.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.h#L56)
- [`_WKAttachment.mm#L136`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L136)
- [`_WKAttachment.mm#L138`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L138)
- [`_WKAttachment.mm#L141`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L141)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
