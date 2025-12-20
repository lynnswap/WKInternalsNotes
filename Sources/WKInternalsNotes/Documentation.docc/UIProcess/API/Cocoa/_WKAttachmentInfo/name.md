# ``WKInternalsNotes/_WKAttachmentInfo/name``

添付ファイル名を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, nullable) NSString *name;
```

## Default Value
`fileWrapper.filename` が空の場合は `preferredFilename` を使う。

## Discussion
`doWithFileWrapper` で取得した `NSFileWrapper` から `filename` を優先して返し、空の場合は `preferredFilename` を返す。

## References
- [`_WKAttachment.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.h#L44)
- [`_WKAttachment.mm#L77`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L77)
- [`_WKAttachment.mm#L80`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L80)
- [`_WKAttachment.mm#L81`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L81)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
