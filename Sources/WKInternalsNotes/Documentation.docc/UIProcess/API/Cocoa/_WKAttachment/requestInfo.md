# ``WKInternalsNotes/_WKAttachment/requestInfo(_:)``

添付情報を同期的に返す（非推奨）。

## Objective-C Declaration
```objective-c
- (void)requestInfo:(void(^)(_WKAttachmentInfo * _Nullable, NSError * _Nullable))completionHandler WK_API_DEPRECATED_WITH_REPLACEMENT("-info", macos(10.14, 10.14.4), ios(12.0, 12.2));
```

## Discussion
`completionHandler` に `self.info` と `nil` をそのまま渡す。

## References
- [`_WKAttachment.h#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.h#L61)
- [`_WKAttachment.mm#L144`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L144)
- [`_WKAttachment.mm#L146`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L146)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
