# ``WKInternalsNotes/_WKAttachmentInfo/shouldPreserveFidelity``

忠実度維持が必要かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL shouldPreserveFidelity WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
`associatedElementType` が `Source` の場合に `YES` を返す。

## References
- [`_WKAttachment.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.h#L48)
- [`_WKAttachment.mm#L112`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L112)
- [`_WKAttachment.mm#L114`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L114)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
