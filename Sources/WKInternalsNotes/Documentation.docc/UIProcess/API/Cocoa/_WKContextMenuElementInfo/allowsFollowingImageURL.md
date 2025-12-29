# ``WKInternalsNotes/_WKContextMenuElementInfo/allowsFollowingImageURL``

画像 URL の追従を許可するかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL allowsFollowingImageURL WK_API_AVAILABLE(macos(26.0));
```

## Default Value
`false`。

## Discussion
`ContextMenuContextData` の `allowsFollowingImageURL` を保持した値を返す。

## References
- [`_WKContextMenuElementInfo.mm#L76`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKContextMenuElementInfo.mm#L76)
- [`APIContextMenuElementInfoMac.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIContextMenuElementInfoMac.h#L62)
- [`_WKContextMenuElementInfo.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKContextMenuElementInfo.h#L41)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
