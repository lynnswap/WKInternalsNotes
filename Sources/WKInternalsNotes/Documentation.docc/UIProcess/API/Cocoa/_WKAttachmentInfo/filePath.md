# ``WKInternalsNotes/_WKAttachmentInfo/filePath``

添付のファイルパスを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, nullable) NSString *filePath;
```

## Default Value
初期化時に `attachment.filePath()` から取得した値を保持する。

## Discussion
`initWithAttachment:` で保持した `_filePath` をそのまま返す。

## References
- [`_WKAttachment.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.h#L45)
- [`_WKAttachment.mm#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L61)
- [`_WKAttachment.mm#L86`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L86)
- [`_WKAttachment.mm#L88`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L88)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
