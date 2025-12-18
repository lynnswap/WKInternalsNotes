# ``WKInternalsNotes/WKUserContentController/_userStyleSheets``

登録済み user style sheets を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSArray<_WKUserStyleSheet *> *_userStyleSheets WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
未登録の場合は空配列。

## Discussion
`userStyleSheets()` の結果を `NSArray` にラップして返す。

## References
- [`WKUserContentControllerPrivate.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentControllerPrivate.h#L48)
- [`WKUserContentController.mm#L294`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentController.mm#L294)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
