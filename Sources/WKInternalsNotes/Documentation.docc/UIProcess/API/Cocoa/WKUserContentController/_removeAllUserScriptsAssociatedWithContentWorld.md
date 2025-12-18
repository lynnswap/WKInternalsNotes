# ``WKInternalsNotes/WKUserContentController/_removeAllUserScriptsAssociatedWithContentWorld(_:)``

指定 content world の user script を全削除する。

## Objective-C Declaration
```objective-c
- (void)_removeAllUserScriptsAssociatedWithContentWorld:(WKContentWorld *)contentWorld WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
`removeAllUserScripts` を呼び出し、指定 world の user script を削除する。

## References
- [`WKUserContentControllerPrivate.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentControllerPrivate.h#L37)
- [`WKUserContentController.mm#L253`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentController.mm#L253)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
