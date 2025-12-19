# ``WKInternalsNotes/WKWebView/_insertAttachmentWithFileWrapper(_:contentType:options:completion:)``

`_insertAttachmentWithFileWrapper` を実行する。

## Objective-C Declaration
```objective-c
- (_WKAttachment *)_insertAttachmentWithFileWrapper:(NSFileWrapper *)fileWrapper contentType:(NSString *)contentType options:(_WKAttachmentDisplayOptions *)options completion:(void(^)(BOOL success))completionHandler WK_API_DEPRECATED_WITH_REPLACEMENT("-_insertAttachmentWithFileWrapper:contentType:completion:", macos(10.14.4, 10.14.4), ios(12.2, 12.2));
```

## Discussion
`completion` に結果を返す。

## References
- [`WKWebViewPrivate.h#L300`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L300)
- [`WKWebView.mm#L5030`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5030)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
