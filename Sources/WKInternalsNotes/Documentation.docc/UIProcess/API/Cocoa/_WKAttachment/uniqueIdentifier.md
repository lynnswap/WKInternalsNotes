# ``WKInternalsNotes/_WKAttachment/uniqueIdentifier``

添付の識別子を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *uniqueIdentifier;
```

## Discussion
内部の `Attachment` が持つ identifier を `NSString` に変換して返す。

## References
- [`_WKAttachment.h#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.h#L57)
- [`_WKAttachment.mm#L181`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L181)
- [`_WKAttachment.mm#L183`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L183)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
