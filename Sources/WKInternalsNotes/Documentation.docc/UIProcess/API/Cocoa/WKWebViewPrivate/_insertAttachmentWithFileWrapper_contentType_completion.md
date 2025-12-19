# ``WKInternalsNotes/WKWebView/_insertAttachmentWithFileWrapper(_:contentType:completion:)``

`_insertAttachmentWithFileWrapper` を実行する。

## Objective-C Declaration
```objective-c
- (_WKAttachment *)_insertAttachmentWithFileWrapper:(NSFileWrapper *)fileWrapper contentType:(NSString *)contentType completion:(void(^)(BOOL success))completionHandler WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
`completion` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L302`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L302)
- [`API/Cocoa/WKWebView.mm#L5033`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5033)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
