# ``WKInternalsNotes/_WKAttachment/setFileWrapper(_:contentType:completion:)``

添付のファイルラッパーと Content-Type を更新する。

## Objective-C Declaration
```objective-c
- (void)setFileWrapper:(NSFileWrapper *)fileWrapper contentType:(nullable NSString *)contentType completion:(void(^ _Nullable)(NSError * _Nullable))completionHandler WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
添付が無効な場合は `WKErrorDomain` のエラーを返して終了する。正常時はファイルパスをクリアし、`setFileWrapperAndUpdateContentType` で内容を更新したあと `updateAttributes` を行い、完了時に `completionHandler(nil)` を呼び出す。

## References
- [`_WKAttachment.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.h#L54)
- [`_WKAttachment.mm#L149`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L149)
- [`_WKAttachment.mm#L151`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L151)
- [`_WKAttachment.mm#L159`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L159)
- [`_WKAttachment.mm#L161`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAttachment.mm#L161)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
