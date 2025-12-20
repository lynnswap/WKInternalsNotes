# ``WKInternalsNotes/_WKAttachmentInfo/data``

添付のデータ本体を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, nullable) NSData *data;
```

## Default Value
ファイルラッパーが通常ファイルでない場合は `nil` を返す。

## Discussion
`doWithFileWrapper` で `NSFileWrapper` を取り出し、通常ファイルなら `regularFileContents` を返す。ディレクトリの `NSFileWrapper` は `nil` になる（実装内に TODO コメントあり）。

## References
- [`_WKAttachment.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.h#L46)
- [`_WKAttachment.mm#L67`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L67)
- [`_WKAttachment.mm#L70`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L70)
- [`_WKAttachment.mm#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L72)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
