# ``WKInternalsNotes/_WKAttachment/setData(_:newContentType:newFilename:completion:)``

宣言のみ確認（実装未調査）。

## Objective-C Declaration
```objective-c
- (void)setData:(NSData *)data newContentType:(nullable NSString *)newContentType newFilename:(nullable NSString *)newFilename completion:(void(^ _Nullable)(NSError * _Nullable))completionHandler WK_API_DEPRECATED_WITH_REPLACEMENT("Please use -setFileWrapper:contentType:completion: instead.", macos(10.13.4, 10.14.4), ios(11.3, 12.2));
```

## Discussion
実装未調査。宣言と対応実装の確認が必要。

## References
- [`_WKAttachment.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.h#L62)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
