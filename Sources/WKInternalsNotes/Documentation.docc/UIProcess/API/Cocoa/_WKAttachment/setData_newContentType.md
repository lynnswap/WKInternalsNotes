# ``WKInternalsNotes/_WKAttachment/setData(_:newContentType:)``

データから添付内容を更新する。

## Objective-C Declaration
```objective-c
- (void)setData:(NSData *)data newContentType:(NSString *)newContentType;
```

## Discussion
`data` から `NSFileWrapper` を生成し、`setFileWrapper:contentType:completion:` を `completion:nil` で呼び出す。

## References
- [`_WKAttachmentInternal.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachmentInternal.h#L43)
- [`_WKAttachment.mm#L167`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L167)
- [`_WKAttachment.mm#L169`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L169)
- [`_WKAttachment.mm#L170`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L170)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
