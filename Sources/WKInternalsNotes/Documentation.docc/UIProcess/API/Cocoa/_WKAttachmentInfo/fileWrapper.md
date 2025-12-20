# ``WKInternalsNotes/_WKAttachmentInfo/fileWrapper``

添付の `NSFileWrapper` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, nullable) NSFileWrapper *fileWrapper;
```

## Discussion
`doWithFileWrapper` で取得した `NSFileWrapper` をそのまま返す。実装コメントでは、QuickLook のサムネイル処理と同時アクセスになる可能性があり、スレッドセーフではない点が指摘されている。

## References
- [`_WKAttachment.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.h#L47)
- [`_WKAttachment.mm#L91`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L91)
- [`_WKAttachment.mm#L93`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L93)
- [`_WKAttachment.mm#L98`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L98)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
