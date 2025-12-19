# ``WKInternalsNotes/WKWebView/_insertAttachmentWithFilename(_:contentType:data:options:completion:)``

`_insertAttachmentWithFilename` を実行する。

## Objective-C Declaration
```objective-c
- (_WKAttachment *)_insertAttachmentWithFilename:(NSString *)filename contentType:(NSString *)contentType data:(NSData *)data options:(_WKAttachmentDisplayOptions *)options completion:(void(^)(BOOL success))completionHandler WK_API_DEPRECATED_WITH_REPLACEMENT("-_insertAttachmentWithFileWrapper:contentType:options:completion:", macos(10.13.4, 10.14.4), ios(11.3, 12.2));
```

## Discussion
`completion` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L300`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L300)
- [`API/Cocoa/WKWebView.mm#L5023`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5023)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
