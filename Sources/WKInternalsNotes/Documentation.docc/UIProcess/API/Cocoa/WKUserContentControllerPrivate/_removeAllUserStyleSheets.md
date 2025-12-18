# ``WKInternalsNotes/WKUserContentController/_removeAllUserStyleSheets()``

登録済み user style sheet を全削除する。

## Objective-C Declaration
```objective-c
- (void)_removeAllUserStyleSheets WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Discussion
`removeAllUserStyleSheets` を呼び出して全削除する。

## References
- [`WKUserContentControllerPrivate.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentControllerPrivate.h#L51)
- [`WKUserContentController.mm#L309`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentController.mm#L309)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
