# ``WKInternalsNotes/_WKAttachment/setData(_:newContentType:newFilename:completion:)``

データから添付内容を更新し、必要ならファイル名も設定する。

## Objective-C Declaration
```objective-c
- (void)setData:(NSData *)data newContentType:(nullable NSString *)newContentType newFilename:(nullable NSString *)newFilename completion:(void(^ _Nullable)(NSError * _Nullable))completionHandler WK_API_DEPRECATED_WITH_REPLACEMENT("Please use -setFileWrapper:contentType:completion: instead.", macos(10.13.4, 10.14.4), ios(11.3, 12.2));
```

## Discussion
`data` から `NSFileWrapper` を生成し、`newFilename` が指定されている場合は `preferredFilename` を設定する。最後に `setFileWrapper:contentType:completion:` を呼び出して更新する。

## References
- [`_WKAttachment.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.h#L62)
- [`_WKAttachment.mm#L173`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L173)
- [`_WKAttachment.mm#L175`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L175)
- [`_WKAttachment.mm#L176`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L176)
- [`_WKAttachment.mm#L178`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L178)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
