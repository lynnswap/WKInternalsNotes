# ``WKInternalsNotes/WKContextMenuElementInfo/_activatedElementInfo``

Context menu の要素情報から _WKActivatedElementInfo を生成して返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, readonly) _WKActivatedElementInfo *_activatedElementInfo;
```

## Default Value
`_elementInfo->interactionInformation()` と `userInfo` を渡して生成した `_WKActivatedElementInfo`。

## Discussion
`TARGET_OS_IPHONE` のみで提供され、`_elementInfo` が保持する `interactionInformation` と `userInfo` を `_WKActivatedElementInfo` の `activatedElementInfoWithInteractionInformationAtPosition:userInfo:` に渡して生成する。アクセスのたびに新規作成される。

## References
- [`WKContextMenuElementInfoPrivate.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContextMenuElementInfoPrivate.h#L34)
- [`WKContextMenuElementInfo.mm#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContextMenuElementInfo.mm#L59)
- [`_WKActivatedElementInfoInternal.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfoInternal.h)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
