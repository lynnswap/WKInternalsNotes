# ``WKInternalsNotes/_WKAttachmentInfo/contentType``

添付の Content-Type を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, nullable) NSString *contentType;
```

## Default Value
初期化時に保持した MIME type が空の場合は UTI type を返す。

## Discussion
`initWithAttachment:` で保持した `_mimeType` が空でなければそれを返し、空の場合は `_utiType` を返す。

## References
- [`_WKAttachment.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.h#L43)
- [`_WKAttachment.mm#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L60)
- [`_WKAttachment.mm#L104`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L104)
- [`_WKAttachment.mm#L106`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L106)
- [`_WKAttachment.mm#L109`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L109)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
